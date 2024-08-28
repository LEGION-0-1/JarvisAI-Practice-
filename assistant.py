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

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    print(f"Searching Google for {query}...")
    speak(f"Searching Google for {query}")
    webbrowser.open(search_url)

def conditions(command):
    site_links = {
        "youtube": "https://www.youtube.com",
        "yt": "https://www.youtube.com",
        "github": "https://github.com/LEGION-0-1",
        "chatgpt": "https://chatgpt.com/",
        "gpt": "https://chatgpt.com/",
    }
    app_path = {
        "calc": 'C:\\Windows\\System32\\calc.exe',
        "notepad": 'C:\\Windows\\System32\\notepad.exe',
        "wordpad": 'C:\\Windows\\System32\\write.exe'
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
                subprocess.Popen(path)
                return
        speak("Sorry, I don't recognize that app.")
        print("Sorry, I don't recognize that app.")

    else:
        speak("Sorry, I didn't understand the command.")
        print("Sorry, I didn't understand the command.")

while True:
    print("How may I assist you?")
    user_input = input()
    conditions(user_input)
