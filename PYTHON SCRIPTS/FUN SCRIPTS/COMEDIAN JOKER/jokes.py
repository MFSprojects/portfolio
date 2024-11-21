#!/bin/python3

import pyjokes
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Find and set the American accent voice
for voice in voices:
    if "en_US" in voice.id:  # Look for an American English voice
        engine.setProperty('voice', voice.id)
        break

# Adjust speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

# Define the function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define the function to tell a joke
def joke():
    speak(pyjokes.get_joke())

# Main execution
if __name__ == "__main__":
    joke()


    
