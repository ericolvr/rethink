# Rethink #


## Start RethinkDB ##
```shell
1) docker compose up -d
```
## Install Dependencies  ##
```shell
1) pip install -r requirements.txt 
```

## Run APP  ##
```shell
1) python main.app 
```

## See Events ##
```shell
1) Open http://localhost:8000
2) Insert Events - See Rethink above
```


## Rethink ##
```shell
1) Open http://localhost:8080
2) Click Tables
3) Click + Add Tables
4) Create Table messages
5) Click Data Explorer
6) Paste: r.db("test").table("messages").insert({"content": "Nova mensagem"}) in Data Explorer Input
7) Click Run Button

-) To see Data
8) Click Tables 
9) Click Messages - on the page bottom - Table Viewer
```


### Software ##
- Python
- RethinkDB  ( NoSQL )
- Docker




