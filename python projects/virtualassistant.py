import speech_recognition as sr

listerner = sr.Recognizer()

try:
  with sr.Microphone() as source:
      print("listening")
      voice = listerner.listen(source)
      command = listerner.recognize_google(voice)
      print(command)
except:
  pass