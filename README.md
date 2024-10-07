# -Voice-Controlled-Personal-Assistant-
This is a simple **Voice-Controlled Personal Assistant** using Python libraries such as `speech_recognition`, `pyttsx3`, `requests`, and `webbrowser`. The assistant listens to voice commands, processes them, and performs tasks like opening websites, playing music, and fetching the latest news.

### Features:
1. **Voice Commands**: The assistant responds to voice commands such as "open Google," "play [song name]," and more.
2. **News Reader**: Reads out the latest news headlines from **NewsAPI.org**. 
3. **Music Playback**: Plays music from predefined links in `musicLibrary`.
4. **Web Browsing**: Opens websites like Google, Facebook, YouTube, and LinkedIn via voice commands.
5. **Stop Functionality**: You can stop the assistant by saying "stop" or "bye."

---

## Setup Instructions

### Prerequisites:
1. **Python 3.x** installed on your system.
2. Required Python libraries:
   - `speech_recognition`
   - `pyttsx3`
   - `webbrowser`
   - `requests`
   
3. **NewsAPI** key:
   - Sign up on [NewsAPI.org](https://newsapi.org/) and get an API key for fetching news headlines.

### Installing Required Libraries:

You can install the required libraries by running:

```bash
pip install SpeechRecognition pyttsx3 requests
```

### Cloning the Project:

1. Clone the project or copy the code into a Python file (`assistant.py`).
2. Create a separate Python file for the music library called `musicLibrary.py`.

Example `musicLibrary.py`:

```python
music = {
    "fein": "https://www.youtube.com/watch?v=B9synWjqBn8",
    "eyes": "https://www.youtube.com/watch?v=pildU9lK6vM",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "rockstar": "https://www.youtube.com/watch?v=UceaB4D0jpo",
    "god's plan": "https://www.youtube.com/watch?v=xpVfcZ0ZcFM",
    "sicko mode": "https://www.youtube.com/watch?v=6ONRf7h3Mdk",
    "humble": "https://www.youtube.com/watch?v=tvTRZJ-4EyI",
    "bodak yellow": "https://www.youtube.com/watch?v=PEGccV-NOm8"
}
```

### Setting Up the API Key:

1. Go to the **NewsAPI** website and get your API key.
2. Replace the empty string in the code with your API key:

```python
newsapi = "YOUR_API_KEY_HERE"
```

### Running the Program:

1. Run the Python script:

```bash
python assistant.py
```

2. The assistant will initialize with the message **"Initializing Jarvis..."**.
3. Speak **"Jarvis"** to activate the assistant.
4. The assistant will listen for a command and perform tasks based on the recognized command.

---

## Voice Commands

### Web Browsing:
- "Open Google" - Opens Google in your web browser.
- "Open Facebook" - Opens Facebook.
- "Open YouTube" - Opens YouTube.
- "Open LinkedIn" - Opens LinkedIn.

### Music Playback:
- "Play [song name]" - Plays the corresponding song from the `musicLibrary`.

Example: 
- "Play fein" - Opens the YouTube link for the song "fein."

### News:
- "News" - Fetches and reads the latest headlines from NewsAPI. After reading each headline, it pauses briefly and listens for the "stop" command. If not stopped, it will proceed to the next article.

### Stop Command:
- "Stop" or "Bye" - Exits the assistant gracefully.

---

## Code Breakdown

### Modules Used:
1. **speech_recognition**: Used to recognize voice input from the user.
2. **pyttsx3**: Provides text-to-speech functionality for the assistant.
3. **webbrowser**: Allows the assistant to open URLs in a web browser.
4. **requests**: Used to send HTTP requests to fetch the latest news from NewsAPI.

### Exception Handling:
- Custom exception `StopProgramException` is raised when the user says "stop" or "bye" to exit the program.
- General exception handling ensures the assistant doesn’t crash due to speech recognition errors.

### Main Loop:
1. The assistant initializes and listens for the keyword "Jarvis."
2. Once activated, it listens for commands and processes them.
3. If a "stop" or "bye" command is detected, the program exits.

---

## Adding More Features:
- To add more voice commands, you can expand the `processCommand` function by adding more `elif` statements.
- For example, to open other websites or trigger different actions based on the recognized command.

---

## Troubleshooting:

1. **Speech Recognition Issues**:
   - If the assistant is having trouble recognizing speech, ensure your microphone is working properly.
   - You can adjust the `timeout` and `phrase_time_limit` parameters in the `listen` function to handle different speaking speeds.

2. **API Issues**:
   - If the news functionality isn’t working, check if the API key is correctly set and ensure your network connection is working.




