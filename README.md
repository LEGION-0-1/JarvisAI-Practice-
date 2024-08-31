# Python Assistant Script

## Overview

This project is a Python-based multi-input command assistant designed to automate various tasks on your computer,
such as opening websites, launching applications, performing searches on Google, YouTube, and GitHub, and playing music playlists.
The script supports both voice and text input, making it versatile and user-friendly.

## Features

- **Voice and Text Input**: Choose between voice or text commands for interaction.
- **Voice Output**: Provides auditory feedback using the `win32com.client` library.
- **Website Access**: Opens popular websites like YouTube, GitHub, ChatGPT, and more based on voice or text commands.
- **Search Functionality**: Performs searches on Google, YouTube, and GitHub based on user input.
- **Application Access**: Opens system applications such as Calculator, Notepad, Wordpad, and others, dynamically finding the application path.
- **Music Playlists**: Choose between different authors' playlists, with an option to select a specific playlist or have one chosen at random.

## Requirements

- **Python 3.x**
- **`pywin32` package**: For voice synthesis (`win32com.client`)
- **`SpeechRecognition` package**: For capturing and processing voice commands
- **`PyAudio` package**: Required for audio input with `SpeechRecognition`

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/LEGION-0-1/Python-Assistant-Script.git
   cd Python-Assistant-Script
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**
   ```bash
   python assistant.py
   ```

## Usage

Once the script is running, it will prompt you with "How may I assist you?" You can choose to interact with the assistant using either voice or text input.

### Commands

- **Open a Website**:
  - "Open YouTube" or "Open YT"
  - "Open GitHub"
  - "Open ChatGPT" or "Open GPT"
  - "Open Spotify"
  
- **Search for Something**:
  - "Search Python tutorials"
  - "Search Python tutorials on YouTube"
  - "Search Python projects on GitHub"
 
- **Launch an Application**:
  - "Launch Calculator"
  - "Launch Notepad"
  - "Launch Wordpad"
  - "Launch Brave"
  - "Launch Unity"
  - "Launch Excel"
  - "Launch PPT"
  - "Launch MS Word"
  - "Launch VS Code"

- **Set reminders**:
  - "Remind me to <task> in <time>" can be used to set a reminder for a particular task
  - Such as
    - "Remind me to walk the dog in 10 minutes"

- **Play Music**:
  - The assistant supports multiple authors' playlists. 
  - It will prompt you to choose an author, and then you can select a specific playlist or allow the assistant to choose one at random.

  Example:
  - "Play Code Vibes"
  - "Play Legion's Code Vibes" (after selecting Legion as the author)
  - "Play a random playlist by Cypher" (after selecting Cypher as the author)

### Voice Commands

If you choose voice input, speak your command clearly when prompted. For example:
- "Open GitHub"
- "Launch Spotify"
- "Play Workout Mix by Legion"

### Text Commands

If you choose text input, type your command and press Enter. For example:
- `Search Python decorators on YouTube`
- `Play Moonlit Melodies by Cypher`

## Extending Functionality

### Adding More Website Commands

To add more commands for opening websites:

1. **Open the `assistant.py` file.**
2. **Locate the `site_links` dictionary** within the `conditions` function.
3. **Add a new entry** in the format `"site_name": "site_url"`.
4. **Handle the new command** by adding logic within the `if command.startswith("open"):` block.

### Adding More Application Commands

To add more commands for launching applications:

1. **Open the `assistant.py` file.**
2. **Locate the `app_path` dictionary** within the `conditions` function.
3. **Add a new entry** in the format `"app_name": "app_path"`.
4. **Handle the new command** by adding logic within the `if command.startswith("launch"):` block.

### Adding More Playlist Commands

To add more playlists:

1. **Open the `assistant.py` file.**
2. **Locate the `playlist_links` dictionary** within the `conditions` function.
3. **Add new entries for different authors and playlists in the format `{"author": {"playlist_name": "playlist_url"}}`.
4. **Handle the new command** by adding logic within the `if command.startswith("play"):` block.


## Contributing

We welcome contributions! Please check the `CONTRIBUTION.md` file for guidelines on how to contribute to this project.

## Issues and Feedback

If you encounter any bugs or have any suggestions for improvements, please open an issue on the [GitHub Issues](https://github.com/LEGION-0-1/Python-Assistant-Script/issues) page.