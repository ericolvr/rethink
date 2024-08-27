import requests
import random
import string
import time


uniorgs = ["001-0001", "001-0002", "001-0003", "001-0004", "001-0005"]
branches = ["Aldeota", "Messejana", "Parangaba", "Embú Guacú", "Parapiacabac"]
alerts = ["Falha de Conexao", "Sensor de Movimento", "Gerador Disparndo", "Porta Aberta", "Alarme de Incendio"]

def send_messages(endpoint, num_messages=100, delay=1):
    for _ in range(num_messages):
    
        uniorg = random.choice(uniorgs)
        branch = random.choice(branches)
        alert = random.choice(alerts)
        data = {"uniorg": uniorg, "branch": branch, "alert": alert}

        # Send the POST request
        response = requests.post(endpoint, json=data)
    

        # Check the response
        if response.status_code != 200:
            print(f"Failed to send message: {data}")
        else:
            print(f"Successfully sent message: {data}")

        # Delay before the next message
        time.sleep(delay)

# Use the function
send_messages('http://127.0.0.1:8000/save-events')