import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi = "your_api_key_here"#get your api key from news.org

class StopProgramException(Exception):
    pass


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):

    #using loop 

    #l=["open google","google","bye"]
    #for i in l:
        #if i in c.lower():
            #webbrowser.open("https://google.com")
            
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        #song=c.lower().split(" ")[1]
        song = c.lower().replace("play ", "")
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()

            articles=data.get('articles',[])

            for article in articles:
                speak(article['title'])
                time.sleep(1) 
                try:
                    with sr.Microphone() as source:
                        print("Listening for 'stop' during news...")
                        audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                        command = recognizer.recognize_google(audio)
                        if "stop" in command.lower():
                            speak("Goodbye!")
                            raise StopProgramException("Stopping news.")
                except sr.UnknownValueError:
                    continue
    elif  "stop" in c.lower() or "bye" in c.lower():
        speak("Goodbye!")
        raise StopProgramException("Exiting due to 'stop' or 'bye' command.") #raising and exception to stop the program by crashing the program
          

if __name__=="__main__":
    speak("Initializing jarvis......")
    while True:
        r=sr.Recognizer()

        try:
           with  sr.Microphone() as source:
               print("listening")
               audio=r.listen(source,timeout=2,phrase_time_limit=1)
           word=r.recognize_google(audio)
           if(word.lower()=="jarvis"):
               speak("Ya")
               
               with  sr.Microphone() as source:
                    print("jarvis activated")
                    audio=r.listen(source,timeout=3,phrase_time_limit=4)
                    command=r.recognize_google(audio)
                    print(command)
                    processCommand(command)
        except StopProgramException as e:
            print(e)
            break   
        except Exception as e:
            print(e)
        
        
        
     

