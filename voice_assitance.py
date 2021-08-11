import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss")
    speak("I am JARVIS, please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

        if "what's the time" in query:
            time = datetime.datetime.now().strftime("%I %M %S %p")
            speak(f"The time now is: {time}")

        if "open chrome" in query.lower():
            webbrowser.get("chrome").open("https://google.com")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
