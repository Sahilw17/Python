import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary
import requests
import openai as OpenAI

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="9f2401e6820d424c9b6aaa5a490f906d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content":command
            }
        ]
    )

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        #Listen for the wake woord Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        def process(c):
           # while True:
                if("open google" in c.lower()):
                    webbrowser.open("https://google.com")
                    speak("Opening Google")
                elif("open youtube" in c.lower()):
                    webbrowser.open("https://youtube.com")
                    speak("Opening YouTube")
                elif("open linkden" in c.lower()):
                    webbrowser.open("https://linkedn.com")
                    speak("Opening linkedn")
                elif c.lower().startswith("play"):
                    song=c.lower().split(" ")[1]
                    link=musiclibrary.music[song]
                    webbrowser.open(link)
                    speak(f"Playing {song}")

                elif c.lower().startswith("news"):
                    r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=9f2401e6820d424c9b6aaa5a490f906d")
                    if r.status_code == 200:
                        data = r.json()
                        
                        # Extract articles
                        articles = data.get('articles', [])
                        
                        for article in articles:
                            speak(article['title'])
                        
                else:
                    #Let openAi handel the request
                    output=aiProcess(c)
                    speak(output)


                    

        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listning.....")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
            command=r.recognize_google(audio)
            print(command)
            if(command.lower()=="jarvis"):
                speak("Yes Master")
            
            #Listen for the command
            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source)
                command=r.recognize_google(audio)

                process(command)


        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except Exception as e:
            print("error... {0}".format(e))