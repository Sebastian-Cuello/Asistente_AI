# Para linux instalar 
# pyttsx3 y libespeak1 (sudo)


import pyttsx3

engine = pyttsx3.init()
engine.say('Hello world!')
engine.runAndWait()