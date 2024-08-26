import win32com.client
import webbrowser

def speak(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)

while 1:
    print("What do you want me to speak")
    s = input()
    site = ["Youtube","Github"]
    link = ["https://www.youtube.com","https://github.com/LEGION-0-1"]
    if(s == f'Open {site[0]}'.lower()):
        speak(f"Opening {site[0]}")
        webbrowser.open(f"{link[0]}")
    elif(s == f'Open {site[1]}'.lower()):
        speak(f"Opening {site[1]}")
        webbrowser.open(f"{link[1]}")