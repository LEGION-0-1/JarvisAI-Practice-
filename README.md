# Python Assistant Script

## Overview

This project is a Python-based voice assistant script designed to automate certain tasks on your computer,
such as opening websites and performing searches on Google, YouTube, and GitHub.
The script uses the `win32com.client` library for voice output and the `webbrowser` module to open URLs.

## Features

- **Voice Output**: Uses the `win32com.client` library to provide auditory feedback.
- **Website Access**: Opens popular websites like YouTube, GitHub, and ChatGPT based on voice commands.
- **Search Functionality**: Performs searches on Google, YouTube, and GitHub based on user input.

## Requirements

- **Python 3.x**
- **`pywin32` package**: For voice synthesis (`win32com.client`)
  - Install via pip: `pip install pywin32`

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/LEGION-0-1/Python-Assistant-Script.git
   cd Python-Assistant-Script
   ```

2. **Install Dependencies**
   ```bash
   pip install pywin32
   ```

3. **Run the Script**
   ```bash
   python assistant.py
   ```

## Usage

Once the script is running, it will prompt you with "How may I assist you?" You can respond with commands like:

- **Open a website**:
  - "Open YouTube" or "Open YT"
  - "Open GitHub"
  - "Open ChatGPT" or "Open GPT"
  
- **Search for something**:
  - "Search Python tutorials"
  - "Search Python tutorials on YouTube"
  - "Search Python projects on GitHub"

The assistant will open the corresponding website or perform the search in your default web browser.

## Adding More Commands

To extend the functionality and add more commands or websites:

1. **Open the `assistant.py` file.**
2. **Locate the `site_links` dictionary** within the `conditions` function.
3. **Add a new entry** in the format `"site_name": "site_url"`.
4. **Handle the new command** by adding logic within the `if command.startswith("open"):` block.

## Contributing

We welcome contributions! Please check the `CONTRIBUTION.md` file for guidelines on how to contribute to this project.

## Issues and Feedback

If you encounter any bugs or have any suggestions for improvements, please open an issue on the [GitHub Issues](https://github.com/LEGION-0-1/Python-Assistant-Script/issues) page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
