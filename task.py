import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
try:
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('Good Morning Vicky')
        elif hour>=12 and hour>=17:
            speak('Good Afternoon Vicky')
        else:
            speak('Good Evening')
        speak('Hellow I am Computer, How can I help you!')
    def takecommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:

            r.pause_threshold=1
            
            audio=r.listen(source,timeout=1,phrase_time_limit=4)
        try:
            
            querry=r.recognize_google(audio,language='en-in')
            
        except Exception:
            
            return 'None'
        return querry


    if __name__ == "__main__":
        while True:
            speak("Tell gh")
            querry=takecommand().lower()
            # Strt
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
            # end
            if "commands" in querry:
                wishme()
                querry=takecommand().lower()
                if 'wikipedia' in querry:
                    speak('Searching wikipedia...')
                    querry=querry.replace('wikipedia','')
                    querry=querry.replace('please','')
                    
                    results=wikipedia.summary(querry,sentences=2)
                    speak('According to wikipedia, ')
                
                    speak(results)
                elif 'who are you' in querry:
                    
                    speak('I am Computer Sir!')
                elif 'made you' in querry:
            
                    speak('I am made by you Sir Waqas powered by Vicky World Production')


                
                elif 'open youtube' in querry:
                    webbrowser.open('youtube.com')
                    speak('Youtube has been opened dear Vicky')
                    
                elif 'open google' in querry:
                    webbrowser.open('google.com')
                    speak('Google Has been opened dear Vicky')
                    
                elif 'stack overflow' in querry:
                    webbrowser.open('stackoverflow.com')
                elif 'stackoverflow' in querry:
                    webbrowser.open('stackoverflow.com')
                elif 'time' in querry:
                    str=datetime.datetime.now().strftime('%H:%M:%S')
                    
                    speak(f"Time is {str}")
                

                elif 'search' in querry:
                    querry=querry.replace('search','')
                    querry=querry.replace('please','')
                    webbrowser.open(querry)
                elif 'song' in querry:
                    music_dir=r'D:\New folder (2)'
                    songs=os.listdir(music_dir)
                
                    os.startfile(os.path.join(music_dir,songs[36]))

                elif 'stop' in querry:
                    
                    speak('Computer has been stopped Thank You Sir!')

                elif 'quit' in querry:
                    
                    speak('Computer has been stopped. Thank You Sir!')
                speak('Again tell what you want to me')
except Exception as e:
    speak('An unknown Error has been occured Check Your Connection Please')