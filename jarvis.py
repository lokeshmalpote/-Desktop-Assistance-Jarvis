import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis sir. please tell me how may i help you")                

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        r.energy_threshold =400
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)    
         
    try:
        print("Recognising.....")
        text = r.recognize_google(audio)
        print(text)
    
    except Exception as e:
        print("say that again please.......")
        return "None"
    return text


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mymail@gmail.com','mypassward')
    server.sendmail('mymail@gmail.com', to,content)  
    server.close()
    
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia......')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
            print('Loop exited')     
        elif 'open youtube' in query:    
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com") 
        elif 'play music' in query:
            music_dir = 'D:\\music'      
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")   
        elif 'open vs code' in query:
            codePath ="C:\\Users\\malpo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     
            os.startfile(codePath)
        elif 'email to lokesh' in query:
            try:
                speak("what would i say?")
                content = takeCommand()
                to ="malpotel628@gmail.com" 
                sendEmail(to,content)   
                speak("Email has been sent !")
            except Exception as e:
                speak("sorry my friend lokesh. i am not able to send at this moment")    
                print("sorry my friend lokesh. i am not able to send at this moment")    
        if 'quit' in query:
            exit()        