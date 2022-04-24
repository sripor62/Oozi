
import smtplib
import pywhatkit as kit
import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')


engine.setProperty('voice',voices[0].id)

author="Stark"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to,content):
    server=smtplib.SMPT('smtp.gmail.com,587')
    server.ehlo()
    server.starttls()
    server.login('srishtiporwal@120202gmail.com','sr232002')
    server.sendmail('your gmail address',to,content)
    server.close()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak(f"Good Morning {author}")
    elif hour>=12 and hour< 18:
        speak(f" Good  Afternoon {author}")
    else:
        speak(f"Good Evening {author}")
    speak(f"Hope you are having a great day ! How may I help you" )

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1.5
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said {query} \n")

    except Exception as e:
        print(f"Sorry {author}, Say that again...")
        return "None"
    return query

if __name__=="__main__":
    # speak(f"Welcome {author}, I am Ooozi")
    wishMe()
    # takeCommand()
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' and 'who' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak(f"According to wikipedia")
            print(results)
            speak(results)
        elif 'news' in query:
            speak("News Headlines")
            query=query.replace("news","")
            url="https://newsapi.org/v2/top-headlines?country=in&apiKey=6b9c2eab1d9a49e789eddfa7e9103dcb"
            news=requests.get(url).text
            news=json.loads(news)
            art=news['articles']

            for article in art:
                print(article['title'])
                speak(article['title'])

                print(article['description'])
                speak(article['description'])
                speak("Moving on to the next news")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'search browser' in query:
            speak("What should I search?")
            um=takeCommand().lower()
            webbrowser.open(f"{um}")

        elif 'ip address' in query:
            ip=requests.get('http://api.ipify.org').text
            print(f"Your ip address is {ip}")
            speak(f"Your ip is {ip}")


        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open ms word' in query:
            codepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
            os.startfile(codepath)

        elif 'open sublime text' in query:
                codepath="G:\\Sublime Text 3\\sublime_text.exe"
                os.startfile(codepath)

        elif 'play music' in query:
            speak("What should I play ?")
            cm=takeCommand().lower()
            kit.playonyt(f"{cm}")

        elif 'send message' in query:
            speak("Who do you want to send the message ? ")
            num=input("Enter number : \n")
            speak("What message you want to send")
            msg=takeCommand().lower()
            speak("When you want to send the message ? ")
            H=int(input("Enter hour\n"))
            M=int(input("Enter minutes\n"))
            kit.sendwhatmsg(num,msg,H,M)

        elif 'send email' in query:
           speak("What should I send ?")
           content=takeCommand().lower()
           speak("Whom to send the email ? Enter email address.")
           to=input("Enter email address : \n")
           sendEmail(to,content)
