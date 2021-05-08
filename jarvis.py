import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywintypes
from win10toast import ToastNotifier 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good morning,Sir')
    elif(hour>=12 and hour<17):
        speak('Good afternoon,Sir')  
    else:
        speak('Good evening,Sir')
    
def goodNight():
    speak('Good night,Sir')

def goodBye():
    speak('Good bye,Sir')

def javisOpeningLine():
    speak('I am jarvis. How can i help you?')

def takeCommand():
    # it takes microphone input from user and returns string output
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Listening...')
        recognizer.pause_threshold=1
        recognizer.energy_threshold=400
        listenedAudio=recognizer.listen(source)
    try:
        print("Recognizing...")
        query=recognizer.recognize_google(listenedAudio,language='en-US')
        print("User said :"+ query)
    except Exception as e:
        print('Say that again please')
        return "None"
    return query

if __name__=="__main__":
   # toast=ToastNotifier()
   # toast.show_toast("Jarvis","Jarvis has been started",duration=30)
    wishMe()
    javisOpeningLine()
    while True:
         commandLine=takeCommand().lower()
         if 'bye' in commandLine:
             speak('Thanks for making me valuable.')
             goodBye()
             break
         elif 'wikipedia' in commandLine:
             speak('Searching wikipedia')
             commandLine=commandLine.replace('wikipedia','')
             speak('According to wikipedia')
             speak(wikipedia.summary(commandLine,sentences=10))
         elif 'open youtube' in commandLine:
             webbrowser.open('Youtube.com')
         elif 'open google' in commandLine:
             webbrowser.open('Google.com')
         elif 'time' in commandLine:
             Time=datetime.datetime.now().strftime("%H:%M:%S")
             speak("Sir,the time is "+Time)
         elif 'vs code' in commandLine:
             vscodePath="C:\\Users\\Prangon Chakraborty\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(vscodePath) 

