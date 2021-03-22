# For linux install
# libespeak1, pyaudio

# For Python 3 
# Pip install pyttsx3, speech_recognition, wikipedia, psutil, pyjokes, pyautogui, wolframalpha.
# Pip pyinstaller is to create an app. command (pyinstaller --onefile "name of app")

import pyttsx3
import datetime
import wikipedia
import smtplib
import psutil
import pyjokes
import os
import pyautogui
import webbrowser as wb
import speech_recognition as sr
import random
import json
import requests
import wolframalpha
import time
from urllib.request import urlopen

engine = pyttsx3.init()
wolframalpha_app_id = '88H2Q8-WHVKA5L4Q6'

# Function to speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function that gives us the current time
def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S") # Reloj 24 horas
    speak("The current time is")
    speak(Time)

# Function that gives us the current date
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

#Function to greetings
def wishme():
    speak("Welcome back Sebastian");
    time_()
    date_()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour <18:
        speak("Good afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")

#Function to recognize the voice / We can take commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

#Function to send emails
#For this function, you must enable low security in you gmail which you are going to use as sender
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com','password')
    server.sendmail('send email')

#function that gives us the cpu and battery usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
    
#function to gives us jokes    
def joke():
    speak(pyjokes.get_joke())

#function to take screenshots
def screenshot():
    img = pyautogui.screenshot()
    img.save('/home/sebastian_cuello/Desktop')

#Main program
if __name__ == "__main__":
    wishme()
    query = takeCommand().lower()
    while query != 'exit':
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak("Searching......")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                #provide reciever email address
                speak("Who is the Reciever?")
                reciever=input("Enter Reciever's Email: ")
                to = reciever
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak("Unable to send Email.")
        elif 'search youtube' in query:
            speak('What should i search?')
            search_Term = takeCommand().lower()
            speak('Here We go to YOUTUBE!')
            wb.open('https://www.youtube.com/results?search_query='+search_Term)
        elif 'search google' in query:
            speak('What should i search?')
            search_Term = takeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'word' in query:
            speak("Open MS word.....")
            ms_word = 'where is the .EXE or the same in linux'
            os.startfile(ms_word)
        elif 'write a note' in query:
            speak("What should i write. Sir")
            notes = takeCommand()
            file = open('notes.txt','w')
            speak("Sir should i include Date and Time")
            ans = takeCommand
            if 'yes' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done taking notes, sir")
            else:
                file.write(notes)
        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            #doesn't work on linux
            screenshot()
        elif 'play music' in query:
            #doesn't work in linux for the moment
            songs_dir = "directory PATH"
            music = os.listdir(songs_dir)
            speak('what should i play?')
            speak('select a number.....')
            ans = takeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('I could not understand you, Please try again')
                ans = takeCommand().lower()
            if 'number' in ans:
                num = int(ans.replace('number',''))
            elif 'random' in ans:
                no = random.randint(1,100)          
            os.startfile(os.path.join(songs_dir,music[num]))
        elif 'remember that' in query:
            speak("What sould i remember")
            memory = takeCommand()
            speak("You asked me remember that" + memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak("You asked me to remember that " + remember.read())
        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=98bd17fbb7b64000b588220821a9c3ef') #NewsAPi is the web that you can get the news with the APIKEY
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top headlines from the Tech Industry')
                print('=============TOP HEADLINES=============='+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+ item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(item['title'])
                    i +=1
            except Exception as e:
                print(str(e))
        elif 'where is ' in query:
            query = query.replace("where is","")
            location = query
            speak("You ask to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is : '+ answer)
            speak('The Answer is '+ answer)
        elif 'what is' in query or 'who is' in query:
            #use the same API wolframalpha
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")
        elif 'stop listening' in query:
            speak('For how many seconds')     
            ans = int(takeCommand())
            time.sleep(ans)
            speak("Sleep mode off")       
        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        query = takeCommand().lower()
        