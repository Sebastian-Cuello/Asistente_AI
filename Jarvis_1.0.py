# Para linux instalar 
# pyttsx3 y libespeak1 (sudo)

import pyttsx3
import datetime

engine = pyttsx3.init()
voice = 'english'

# Función que recibe un string y reproduce en audio dicho string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Función que nos indica el tiempo actual (Tomado desde la computadora)
def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S") # Reloj 24 horas
    speak("The current time is")
    speak(Time)

# Función que nos indica la fecha actual (Tomado desde la computadora)
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

