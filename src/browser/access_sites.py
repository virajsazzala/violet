import re
import webbrowser

from src.consts import ADDRESSING, NICKNAME

import src.senses.speech as speech

PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
searches = {
    "my website": "https://virajsazzala.xyz",
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com/",
    "github": "https://gihub.com/virajsazzala",
    "instagram": "https://www.instagram.com/virajsazzala/",
    "twitter": "https://twitter.com/virajsazzala",
    "anime website": "https://9animetv.to/",
}


def open_browser(url):
    print(f"Accessing {url}")
    webbrowser.get(PATH).open(url)


def search_online(text):
    # key in searches dictionary is found in text then open the corresponding value
    for key in searches.keys():
        if re.search(key, text):
            # generate regex for query on YouTube
            if re.search("on youtube search for", text):
                search_string = (text.split("on youtube search for")[1][:-1]).strip()
                speech.say(
                    f"{ADDRESSING} {NICKNAME}, searching for {search_string} on youtube"
                )
                open_browser(
                    "https://www.youtube.com/results?search_query=" + search_string
                )
            elif re.search("on anime website search for", text):
                search_string = (text.split("on anime website search for")[1][:-1]).strip()
                speech.say(
                    f"{ADDRESSING} {NICKNAME}, searching for {search_string} on anime website"
                )
                open_browser(
                    "https://9animetv.to/search?keyword=" + search_string
                )
            else:
                speech.say(f"{ADDRESSING} {NICKNAME}, opening {key}")
                open_browser(searches[key])


def main():
    pass


if __name__ == "__main__":
    main()
