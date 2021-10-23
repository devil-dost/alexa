from subprocess import run
import speech_recognition as sr
import pywhatkit
import wikipedia
import pyttsx3
import requests
from bs4 import BeautifulSoup
import datetime

from wikipedia.wikipedia import search

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
time1 = datetime.datetime.now().strftime('%H:%M')
engine.say(' the currrent time is  ' + time1)
engine.say('I AM JARVIS IRONMAN vaaali BOT  I AM LISTENING')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('i am listenng')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            engine.say(command)
            engine.runAndWait()
            print(command)
            
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('have some patience dude i will play your song '+ song)
        pywhatkit.playonyt(song)

   

    elif 'video' in command:
        song1 = command.replace('play','')
        talk('have some patience dude i will play your song '+ song1)
        pywhatkit.playonyt(song1)
    
    elif 'search' in command:
        song2 = command.replace('search','')
        talk('i found this  result for '+ song2)
        pywhatkit.search(song2)

    elif 'date' in command:
        talk('sorry, i kaant goo')

    elif 'single' in command:
        talk('no i am not single i am having an affair with wifi')

    elif 'temperature' in command:
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        talk(f"current {search} is {temp}")
        print(f"current {search} is {temp}")

    elif "internet speed" in command:
        import speedtest
        test = speedtest.Speedtest()
        dl = test.download()
        up= test.upload()
        talk(f"the current downloading speed is {dl} bit per second and the current uploading speed is {up} bit per second ")
        print(f"the current downloading speed is {dl} bit per second and the current uploading speed is {up} bit per second ")


    else:
        talk('kindly spit the   pan and then talk')


while True:
    run_alexa()





