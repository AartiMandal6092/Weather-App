import requests
import os
import json #javascript Object Notation  data -> text
city=input("Enter the name of the city : \n")

url="https://api.open-meteo.com/v1/forecast?latitude=26.9124&longitude=75.7873&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url)

weather_dic=response.json()
current = weather_dic["current_weather"]

print(f"City: {city}")
print(f"Temperature: {current['temperature']} °C")
print(f"Wind Speed: {current['windspeed']} km/h")
print(f"Wind Direction: {current['winddirection']}°")


speech_text = f"City {city}. Temperature {current['temperature']} degree Celsius. " \
              f"Wind speed {current['windspeed']} kilometers per hour. " \
              f"Wind direction {current['winddirection']} degrees."
speech_text = speech_text.replace("'", "").replace("°", " degrees")


os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; '
              f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
              f'$speak.Speak(\'{speech_text}\');"')
