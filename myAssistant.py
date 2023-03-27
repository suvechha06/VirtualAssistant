import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("What can I do for you ?") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()       
        if 'jeera' in query:
            print("Yes Boss")
            speak("Yes Boss")

        elif 'who are you' in query:
            print("My name is Jeera. I am you personal assisstant.")
            speak("My name is Jeera. I am you personal assisstant.")

        elif 'what is' in query:
            speak("Searching Wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak("Searching Wikipedia...")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search for' in query:
            speak("Searching Wikipedia...")
            query = query.replace("search for", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open('google.com')

        elif 'open google' in query:
            speak("What should I search")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("What would you like to watch")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'open paint' in query:
            os.system("start mspaint")

        elif 'close paint' in query:
            os.system("taskkill /f /im mspaint.exe")

        elif 'open notepad' in query:
            os.system("start notepad")

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            os.system("restart /r /t 5")

        elif 'lock' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            




