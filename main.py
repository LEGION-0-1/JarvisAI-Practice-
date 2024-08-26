import win32com.client
import webbrowser

def speak(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)

def conditions(s):
    site = ["Youtube", "Github"]
    link = ["https://www.youtube.com", "https://github.com/LEGION-0-1"]
    if(f'Open {site}' or f'Search {site}'):
        if (s == f'Open {site[0]}'.lower()):
            speak(f"Opening {site[0]}")
            webbrowser.open(f"{link[0]}")
        elif (s == f'Open {site[1]}'.lower()):
            speak(f"Opening {site[1]}")
            webbrowser.open(f"{link[1]}")
        elif (s == 'Search'.lower()):
            print("What should I search?")
            a = input()
            webbrowser.open(f"https://www.google.com/search?q={a}")
    else:
        speak(s)

while 1:
    print("What do you want me to speak")
    s = input()
    conditions(s)