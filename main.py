import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("What do you want me to speak")
    s = input()
    speaker.Speak(s)