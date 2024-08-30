import win32com.client
import webbrowser
import subprocess
import shutil
import random
import speech_recognition as sr

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

def choose_playlist(playlists):
    speak("Which playlist would you like to listen to?")
    print("Options:")
    for i, playlist in enumerate(playlists, 1):
        print(f"{i}. {playlist}")
    
    speak("Please select a number or type 'random' for a random choice.")
    choice = input("Enter the number of the playlist or type 'random': ").strip().lower()
    
    if choice == "random":
        selected_playlist = random.choice(list(playlists.items()))
    elif choice.isdigit() and 1 <= int(choice) <= len(playlists):
        selected_playlist = list(playlists.items())[int(choice) - 1]
    else:
        speak("Invalid selection. Please try again.")
        print("Invalid selection. Please try again.")
        return None
    
    return selected_playlist

def play_author_playlist(author_playlists):
    speak("Which author's playlist would you like to listen to?")
    print("Options:")
    for i, author in enumerate(author_playlists.keys(), 1):
        print(f"{i}. {author}")
    
    speak("Please select a number.")
    author_choice = input("Enter the number of the author: ").strip().lower()
    
    if author_choice.isdigit() and 1 <= int(author_choice) <= len(author_playlists):
        selected_author = list(author_playlists.keys())[int(author_choice) - 1]
        selected_playlist = choose_playlist(author_playlists[selected_author])
        if selected_playlist:
            play_music(*selected_playlist)
    else:
        speak("Invalid selection. Please try again.")
        print("Invalid selection. Please try again.")

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

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing the speech recognition service.")
        print("Sorry, I'm having trouble accessing the speech recognition service.")
    return ""

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
    
    author_playlists = {
        "Legion": {
            "Code Vibes": 'https://open.spotify.com/playlist/1B42ovHid4tydXN9j63DNL?si=cec94bd2a69547f4',
        },
        "Cypher": {
            "Moonlit Melodies": 'https://open.spotify.com/playlist/6thefFdcUAFMq3OauiYrI5?si=49fbd68b9cc34a4f',
            "Therapy Session": 'https://open.spotify.com/playlist/1QEYpbmhQmpc5oyuOmrNyM?si=45586524a02f4662',
            "The what if's": 'https://open.spotify.com/playlist/5XZpcWbwdY4F3uE5Tnw7JL?si=a42e0c84dae040f0',
            "Chillin in the Car": 'https://open.spotify.com/playlist/796158DQgVqtmzpW7HJhPL?si=e170db32357046be',
            "Chillin in the Car II": 'https://open.spotify.com/playlist/0h9zoxsjsxBSXorkj1sBLI?si=c4f5f9c4c1774284',
            "New Beginnings": 'https://open.spotify.com/playlist/2W8ayBPPRFOqZsZ6CEFnNU?si=ef1f7b8122c24302',
        }
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
        play_author_playlist(author_playlists)
    
    else:
        speak("Sorry, I didn't understand the command.")
        print("Sorry, I didn't understand the command.")

def main():
    while True:
        
        if input_method == "voice":
            user_input = get_voice_input()
        elif input_method == "text":
            user_input = input("How may I assist you? ")
        else:
            speak("Invalid choice. Please try again.")
            print("Invalid choice. Please try again.")
            continue

        if user_input:
            conditions(user_input)

if __name__ == "__main__":
    speak("Would you like to use voice input or text input?")
    input_method = input("Type 'voice' for voice input or 'text' for text input: ").strip().lower()
    main()