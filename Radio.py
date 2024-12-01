import requests
import vlc
import time
import pyttsx3

url = "https://raw.githubusercontent.com/2shrestha22/radio/main/assets/radio_list.json"
response = requests.get(url)
data = response.json()

f = float(input("Frequency: "))

while True:
    for i in data: # i is a dict
        for key in i:
            if i["frequency"] == f:
                    streamUrl = i["streamUrl"] # Feathing the Stream URL
                    print(f"Frequency {f}")
                    print(f"Playing {i["name"]}")
                    engine = pyttsx3.init()
                    engine.say(f"Playing {i["name"]} Frequency {f}")
                    engine.runAndWait()
                    player = vlc.MediaPlayer()
                    media = vlc.Media(streamUrl)
                    player.set_media(media)
                    player.play()
                    time.sleep(5)
                    f = float(input("Change Frequency: "))
                    player.stop()
                    break

'''
Before using radio you must have VLC Media Player in your system. Also, verify the stream URL (Provided while running) in VLC to Play if it refuge to connect.
'''