import time
import random
import requests

# Discord Token
AUTHORIZATION = ""
# Discord Channel ID
CHANNEL_ID =
# Delay setting
DELAY_IN_SECONDS = False # Switch between seconds and minutes
MIN_DELAY = 1
MAX_DELAY = 1

# A variable for storing the ID of the last sent message
# This could come in handy for your future modifications of this script—for example, for deleting the previous message after sending a new one, etc.
# Currently, this is used exclusively to send the ID of the sent message to the log(as an example).
last_message_id = None

# Insert the message text inside the brackets.
MESSAGE = """ """

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Authorization": AUTHORIZATION,
    "Content-Type": "application/json",
}

def send_message():
    global last_message_id
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'
    data = {"content": MESSAGE, "tts": False}
    
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        if response.ok:
            last_message_id = response.json().get('id')
            print(f"New message successfully sent.. ID: {last_message_id}")
        else:
            print(f"Sending error. Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Sending error: {e}")

def main():
    print("Script started.")
    while True:
        send_message()
        
        # Generate a random number in a given range
        random_value = random.randint(MIN_DELAY, MAX_DELAY)
        
        if DELAY_IN_SECONDS:
            sleep_seconds = random_value
            print(f"Waiting {random_value} seconds before next cycle...\n")
        else:
            sleep_seconds = random_value * 60
            print(f"Waiting {random_value} minutes ({sleep_seconds} sec.) before next cycle...\n")
        
        time.sleep(sleep_seconds)

if __name__ == "__main__":
    main()
