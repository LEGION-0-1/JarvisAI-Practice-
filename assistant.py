import win32com.client
import webbrowser
import subprocess

def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def open_website(site_name, url):
    print(f"Opening {site_name}...")
    speak(f"Opening {site_name}")
    webbrowser.open(url)

def play_music(playlist_name, url):
    print(f"Playing {playlist_name}...")
    speak(f"Playing {playlist_name}")
    webbrowser.open(url)

def open_app(app_name, path):
    print(f"Opening {app_name}...")
    speak(f"Opening {app_name}")
    subprocess.Popen(path)

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    print(f"Searching Google for {query}...")
    speak(f"Searching Google for {query}")
    webbrowser.open(search_url)

def conditions(command):
    site_links = {
        "youtube": "https://www.youtube.com",
        "yt": "https://www.youtube.com",
        "github": "https://github.com/",
        "chatgpt": "https://chatgpt.com/",
        "gpt": "https://chatgpt.com/",
        "spotify": "https://open.spotify.com/",
        "discord": "https://discord.com/app"
    }
    app_path = {
        "calculator": 'C:\\Windows\\System32\\calc.exe',
        "notepad": 'C:\\Windows\\System32\\notepad.exe',
        "wordpad": 'C:\\Windows\\System32\\write.exe',
        "brave": 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\Brave.exe',
        "unity": 'C:\\Program Files\\Unity Hub\\Unity Hub.exe',
        "excel": 'C:\\Program Files\\Microsoft Office\\Office15\\EXCEL.exe',
        "ppt": 'C:\\Program Files\\Microsoft Office\\Office15\\POWERPNT.exe',
        "ms word": 'C:\\Program Files\\Microsoft Office\\Office15\\WINWORD.exe',
        "vs code": 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
    }
    playlist_links = {
        "code vibes": 'https://open.spotify.com/playlist/1B42ovHid4tydXN9j63DNL?si=cec94bd2a69547f4'
    }
    command = command.lower()
    
    if command.startswith("open"):
        for site, link in site_links.items():
            if site in command:
                open_website(site.capitalize(), link)
                return
        speak("Sorry, I don't recognize that site.")
        print("Sorry, I don't recognize that site.")
    
    elif "search" in command:
        search_platform = "google"
        query = command.replace("search", "").strip()
        
        if "on youtube" in command:
            search_platform = "youtube"
            query = query.replace("on youtube", "").strip()
            search_url = f"https://www.youtube.com/results?search_query={query}"
        elif "on github" in command:
            search_platform = "github"
            query = query.replace("on github", "").strip()
            search_url = f"https://github.com/search?q={query}"
        else:
            search_url = f"https://www.google.com/search?q={query}"

        print(f"Searching {search_platform.capitalize()} for {query}...")
        speak(f"Searching {search_platform.capitalize()} for {query}")
        webbrowser.open(search_url)
    elif command.startswith("launch"):
        for app, path in app_path.items():
            if app in command:
                open_app(app.capitalize(), path)
                return
        speak("Sorry, I don't recognize that app.")
        print("Sorry, I don't recognize that app.")
    elif command.startswith("play"):
        for playlist, link in playlist_links.items():
            if playlist in command:
                play_music(playlist.capitalize(), link)
                return
        speak("Sorry, I don't recognize that site.")
        print("Sorry, I don't recognize that site.")

    else:
        speak("Sorry, I didn't understand the command.")
        print("Sorry, I didn't understand the command.")

while True:
    print("How may I assist you?")
    user_input = input()
    conditions(user_input)
