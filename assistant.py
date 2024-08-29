import win32com.client
import webbrowser
import subprocess
import shutil

def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def open_website(site_name, url):
    print(f"Opening {site_name}...")
    speak(f"Opening {site_name}")
    webbrowser.open(url)

def play_music(platform, query=None, playlist_url=None):
    if playlist_url:
        print(f"Playing playlist {query} on {platform}...")
        speak(f"Playing playlist {query} on {platform}")
        webbrowser.open(playlist_url)
    elif query:
        if platform.lower() == "spotify":
            search_url = f"https://open.spotify.com/search/{query.replace(' ', '%20')}"
        elif platform.lower() == "youtube":
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        else:
            speak(f"Sorry, I can't search for music on {platform}.")
            print(f"Sorry, I can't search for music on {platform}.")
            return

        print(f"Searching for {query} on {platform}...")
        speak(f"Searching for {query} on {platform}")
        webbrowser.open(search_url)

def launch_app(app_name):
    app_path = shutil.which(app_name)
    if app_path:
        print(f"Launching {app_name}...")
        speak(f"Launching {app_name}")
        subprocess.Popen(app_path)
    else:
        speak(f"Could not find {app_name} on your system.")
        print(f"Could not find {app_name} on your system.")

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
        app_name = command.replace("launch", "").strip()
        launch_app(app_name)
    
    elif command.startswith("play"):
        if "on spotify" in command:
            query = command.replace("play", "").replace("on spotify", "").strip()
            if query in playlist_links:
                play_music("Spotify", query, playlist_links[query])
            else:
                play_music("Spotify", query)
        elif "on youtube" in command:
            query = command.replace("play", "").replace("on youtube", "").strip()
            play_music("YouTube", query)
        else:
            speak("Please specify a platform, like Spotify or YouTube.")
            print("Please specify a platform, like Spotify or YouTube.")
    
    else:
        speak("Sorry, I didn't understand the command.")
        print("Sorry, I didn't understand the command.")

while True:
    print("How may I assist you?")
    speak("How may I assist you?")
    user_input = input()
    conditions(user_input)
