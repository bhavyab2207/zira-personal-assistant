from logging import exception
from unittest import result
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #taking zira voice female and id=0 is david male voice




def speak(audio):     #to speak the arguments
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning user!")
    elif hour>=12 and hour<12:
        speak("Good Afternoon User!")
    else:
        speak("Good Evening User:")
    speak("This is your personal assistant Whiskey. How may I help you?")


def takecommand():
    #This will take voice command from the user and return string output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        querry = r.recognize_google(audio, language='en-in')
        print(f"User said : {querry}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return querry


#main method use constructor
if __name__ == "__main__":
    wishMe()
    while True:
        querry = takecommand().lower()
        if 'wikipedia' in querry:
            speak("Searching wikipedia......")
            querry = querry.replace('wikipedia',"")
            results = wikipedia.summary(querry, 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
      
        elif 'open youtube' in querry:
            speak("Opening youtube...")
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in querry:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/webhp?ie=UTF-8&rct=j")
        
        elif 'open spotify' in querry:
            speak("Opening spotify...")
            webbrowser.open("https://open.spotify.com/")

        elif 'open netflix' in querry:
            speak("Happy netflix and chill.....")
            webbrowser.open("https://www.netflix.com/browse")
        
        elif 'open valorant' in querry: 
            speak("Opening games....")
            os.startfile("C:\Riot Games\Riot Client\RiotClientServices.exe")
        
        #elif 'write email' in querry:
          #  try:
           #     speak("Speak Content ")
        

              

