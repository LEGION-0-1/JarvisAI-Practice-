import win32com.client
import webbrowser

def speak(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)

def conditions(s):
    site = ["Youtube", "Github", "ChatGPT"]
    link = ["https://www.youtube.com", "https://github.com/LEGION-0-1", "https://chatgpt.com/"]
    if(f'Open {site}' or "Search"):
        if (s == f'open youtube' or s == f'open yt'):
            a = 0
            print(f"Opening {site[a]}...")
            speak(f"Opening {site[a]}")
            webbrowser.open(f"{link[a]}")
        elif (s == f'open github'):
            a = 1
            print(f"Opening {site[a]}...")
            speak(f"Opening {site[a]}")
            webbrowser.open(f"{link[a]}")
        elif (s == f'open chatgpt' or s == f'open gpt'):
            a = 2
            print(f"Opening {site[a]}...")
            speak(f"Opening {site[a]}")
            webbrowser.open(f"{link[a]}")
        elif (s == 'search'):
            b = "What Should I Search?"
            print(b)
            speak(b)
            a = input()
            speak(f"Searching {a}")
            webbrowser.open(f"https://www.google.com/search?q={a}")

while 1:
    print("How may i assist you?")
    s = input()
    speak(s)
    conditions(s.lower())