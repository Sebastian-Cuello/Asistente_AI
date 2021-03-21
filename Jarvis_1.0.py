# For linux install
# libespeak1, pyaudio

# For Python 3 
# Pip pyttsx3, speech_recognition, wikipedia, psutil, pyjokes

import pyttsx3
import datetime
import wikipedia
import smtplib
import psutil
import pyjokes
import os
import webbrowser as wb
import speech_recognition as sr

engine = pyttsx3.init()

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
    
def joke():
    speak(pyjokes.get_joke())

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
            file = open('notes.txt'.'w')
            speak("Sir should i include Date and Time")
            ans = takeCommand
            if 'yes' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done taking notes, sir")
            else
                file.write(notes)
        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt'.'r')
            print(file.read())
            speak(file.read())
        
        query = takeCommand().lower()
        