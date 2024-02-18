import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# responsible for handling the text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
# responsible for getting the audio from microphone
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
# responsible for setting reminder
def set_reminder():
    speak("What should I remind you?")
    reminder_text = get_audio()
    
    if reminder_text:
        now = datetime.datetime.now()
        reminder_time = now + datetime.timedelta(minutes=5)  # Set a reminder for 5 minutes from now
        formatted_time = reminder_time.strftime("%H:%M %p")
        speak(f"I will remind you to {reminder_text} at {formatted_time}")
        # Here you can implement a reminder system (e.g., using a timer or scheduler)
# responsible for creating todo list
def create_todo_list():
    speak("What tasks would you like to add to your to-do list?")
    todo_text = get_audio()

    if todo_text:
        # Here you can implement a to-do list system (e.g., store tasks in a file or database)
        speak(f"Added '{todo_text}' to your to-do list.")
# responsible for search the web
def search_web():
    speak("What would you like to search for?")
    search_query = get_audio()

    if search_query:
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        webbrowser.open(search_url)
        speak(f"Here are the search results for '{search_query}'.")

# Main loop
while True:
    speak("How can I assist you?")
    command = get_audio()

    if "reminder" in command:
        set_reminder()
    elif "to-do list" in command:
        create_todo_list()
    elif "search" in command or "web" in command:
        search_web()
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        break
    else:
        speak("Sorry, I didn't understand that. Can you please repeat?")
