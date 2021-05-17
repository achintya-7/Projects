import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english+f2')
engine.setProperty('rate', 178)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=19:
        speak("Good Evening")
    else:
        speak("It is late night, sir")
  
    time.sleep(1)

    speak("Hello, I am an Assistant, please give me a command")


def Commands():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')   
        print(f"User said: {query}\n")

    except Exception as e:
            print("Say that again please......")
            return "None"
    return query
         
if __name__ == "__main__":
    Wishme()
    while 1:
        query = Commands().lower()

        if 'wikipedia' in query:
            speak("Searching wiki")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            #print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'stop' in query:
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
