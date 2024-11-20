#!/bin/python3

import pyjokes
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Find and set an American English voice
for voice in voices:
    if "en_US" in voice.id:  # Check for American English
        engine.setProperty('voice', voice.id)
        break

# Adjust speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

# Function to speak the audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to tell a joke
def joke():
    speak(pyjokes.get_joke())

# Main execution
if __name__ == "__main__":
    joke()
