import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")   
                 # use the default microphone as the audio source
    audio = r.listen(source,timeout=1,phrase_time_limit=10)                  # listen for the first phrase and extract it into audio data


print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
                          # speech is unintelligible
print("Could not understand audio")