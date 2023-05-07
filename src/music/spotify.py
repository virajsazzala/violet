import os
import re
from src.consts import NICKNAME, ADDRESSING, SPOTIFY_DIR
import src.senses.speech as speech


def prompt():
    speech.say(f"Would you like to search for a song or enter a link?")
    text = speech.listen()
    if re.search("search", text):
        speech.say(f"Which song would you like to download?")
        song = (speech.listen())[:-1]
        download(song)
    elif re.search("link", text):
        speech.say(f"Please enter the link of the song you would like to download")
        song = input("Enter song URL: ")
        download(song)
    else:
        speech.say(f"Sorry, I didn't catch that.")


def download(query):
    speech.say(f"{ADDRESSING} {NICKNAME}, Downloading now!")
    os.system(f"cd {SPOTIFY_DIR} && spotdl download {query}")
    speech.say("Download complete!")


def main():
    pass


if __name__ == "__main__":
    main()
