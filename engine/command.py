import pyttsx3
import speech_recognition as sr 
import pyaudio as audio
import eel


# Creating the function to make the assistant speak
def speak(text):
    #initiating the voices
    engine = pyttsx3.init("sapi5")

    #getting the voices our system has.
    voices = engine.getProperty('voices')
    print(voices)

    #Selecting the voice
    engine.setProperty('voice', voices[0].id)

    #Specifying the auido rate
    engine.setProperty('rate', 174)

    # Initiating it to speak.
    engine.say(text)
    engine.runAndWait()

# checking the function.
# speak("Hey there this is you cortix ai")

# Creating the function for speech recognition.
@eel.expose
def TakeCommand():
    # initializing the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source :
        print("Listening....")
        # Displaying it in app
        eel.DisplayMessage("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source , 10 , 8)


    try:
        print("Recognizing...")
        # Displaying it in app
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")
        # Displaying it in app
        eel.DisplayMessage(query)
        speak(query)
        eel.DisplayHood()
    except Exception as e:
        return ""
    
    return query.lower()

