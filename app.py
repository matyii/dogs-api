import requests, time
from discord_webhook import DiscordWebhook

dogs = "https://dog.ceo/api/breeds/image/random"
webhook_url = "URL"
# webhook_url = ['url', 'url2']

wait_time = int(input('Time interval between each picture (in seconds): '))
number_of_pictures = input('How many pictures you want to send? (number or "i" for infinity): ')

def doggo():
        webhook = DiscordWebhook(url=webhook_url, content=requests.get(dogs).json()["message"]).execute()
        time.sleep(wait_time)

if number_of_pictures == "i":
    while 1:
        doggo()
else:
    for i in range(int(number_of_pictures)):
        doggo()