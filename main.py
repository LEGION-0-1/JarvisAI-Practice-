import win32com.client
import webbrowser

def speak(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)

def conditions(s):
    site = ["Youtube", "Github"]
    link = ["https://www.youtube.com", "https://github.com/LEGION-0-1"]
    if(f'Open {site}' or "Search"):
        if (s == f'Open {site[0]}'.lower()):
            speak(f"Opening {site[0]}")
            webbrowser.open(f"{link[0]}")
        elif (s == f'Open {site[1]}'.lower()):
            speak(f"Opening {site[1]}")
            webbrowser.open(f"{link[1]}")
        elif (s == 'Search'.lower()):
            b = "What Should I Search?"
            print(b)
            speak(b)
            a = input()
            speak(f"Searching {a}")
            webbrowser.open(f"https://www.google.com/search?q={a}")

while 1:
    print("What do you want me to speak")
    s = input()
    speak(s)
    conditions(s)