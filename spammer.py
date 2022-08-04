import requests
from time import sleep

token = {"authorization":"PASTE YOUR TOKEN HERE"}


channel_id = int(input("Channel ID: "))
message = input("Message to spam: ")
amount = int(input("How many messages?: "))

for i in range(0,amount):
    req = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json={"content":message}, headers=token)
    print(f"Sending {message} in {channel_id}")
    sleep(0.3)
    

    

