import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  #pip install speech recognization
import datetime #pip install datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowsser
import os

engine = pyttsx3.init('sapi5')  #sapi5 microsoft voice api
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Welocome and good morning")
        speak("hope u are doing ok")

    elif hour>=12 and hour<18:
        speak("Welocome and good afternoon")
        speak("hope u are doing ok")

    else:
        speak("Welocome and good evening")
        speak("hope u are doing ok")

    speak("I am alex how may i help you today?")  


#make sure that u have install the pyaudio module in order to listen the command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...!")
        query  = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please.....!")
        return "None"      
    return query       

if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...!')
            quary  = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            print(result)
            speak(result)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open mangafreak' in query:
            webbrowser.open("w11.mangafreak.net")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Daksh the time is {strTime}")

        elif 'visual studio code' in query:
            codePath = "D: \\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'shutdown' in query:
            shutdown = input("Do you wish to shutdown your computer ? (yes / no):")
            if shutdown == 'no':
                exit()
            else:
                os.system("shutdown /s /t 1")
           
        elif 'open spotify' in query:
            webbrowser.open("www.spotify.com")

            //dcpd.sst38@cumail. in
