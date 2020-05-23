import pyttsx3
import speech_recognition as sr
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=3)
    try:
        querry=r.recognize_google(audio,language="en-in")
        print(f"You Said {querry}")
    except Exception:
        print('Say That Again Please!')
        return 'None'
    return querry
if __name__ == "__main__":
    querry=takecommand()
    querry=querry.lower()
    if "poweroff computer" in querry:
        speak("Computer has been closed")
        os.system("shutdown /s /t 1")
    if "power off computer" in querry:
        speak("Computer has been closed")
        os.system("shutdown /s /t 1")
    if "power of computer" in querry:
        speak("Computer has been closed")
        os.system("shutdown /s /t 1")
    if "quit Computer" in querry:
        speak("Computer has been power off")
        os.system("shutdown /s /t 1")
    if "restartcomputer" in querry:
        speak("We restarting your PC")
        os.system("shutdown /r /t 1")
    if "restart computer" in querry:
        speak("We restarting your PC")
        os.system("shutdown /r /t 1")
    if "rstart computer" in querry:
        speak("We restarting your PC")
        os.system("shutdown /r /t 1")
    if "restart Computer" in querry:
        speak("We restarting your PC")
        os.system("shutdown /r /t 1")
    
        

