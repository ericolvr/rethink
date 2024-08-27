"""base to study about rethink """
from rethinkdb import RethinkDB
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from typing import Generator

app = FastAPI()

r = RethinkDB()
def get_rethinkdb_connection():
    return r.connect("localhost", 28015)


def listen_to_changes() -> Generator[str, None, None]:
    connection = get_rethinkdb_connection()
    table = r.db("test").table("messages")
    cursor = table.changes().run(connection)

    for change in cursor:
        yield f"data: {change['new_val']}\n\n"


"""
    The HTML content is a simple page with a table that will be populated with the messages received from the server.
    This page using this Javascript should be on Smart Integration - Terminal - to accept real time events 
"""
@app.get("/", response_class=HTMLResponse)
async def get():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Live Updates</title>
        <style>
            body {
                margin: 0;
                padding: 0;
            }
            .topbar {
                width: 100%;
                height: 50px;
                background-color: #EFEFEF;
                color: #00000;
                text-align: center;
                line-height: 50px;
            }
            .container {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            table {
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
        </style>
    </head>
    <body>
        <div class="topbar">Terminal recebendo Eventos via SSE ( Server Side Events )</div>
        <div class="container">
            <table id="messages"></table>
        </div>
        <script type="text/javascript">
            const evtSource = new EventSource("/events");
            evtSource.onmessage = function(event) {
                const newElement = document.createElement("tr");
                const newCell = document.createElement("td");
                newCell.textContent = event.data;
                newElement.appendChild(newCell);
                document.getElementById("messages").appendChild(newElement);
            };
        </script>
    </body>
    </html>
    """
    return html_content


@app.get("/events")
async def events():
    return StreamingResponse(listen_to_changes(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000
    )


