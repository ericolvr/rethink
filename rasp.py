import requests
import random
import string
import time

def send_messages(endpoint, num_messages=100, delay=1):
    for _ in range(num_messages):
        # Generate a random message
        message = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        data = {'message': message}

        # Send the POST request
        response = requests.post(endpoint, json=data)

        # Check the response
        if response.status_code != 200:
            print(f"Failed to send message: {message}")
        else:
            print(f"Successfully sent message: {message}")

        # Delay before the next message
        time.sleep(delay)

# Use the function
send_messages('http://127.0.0.1:8000/save-events')