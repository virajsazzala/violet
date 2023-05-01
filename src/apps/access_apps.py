import subprocess

import src.senses.speech as speech
from src.consts import ADDRESSING, NICKNAME

# TODO: add more apps
apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
}


def open_app(app):
    speech.say(f"{ADDRESSING} {NICKNAME}, Opening {app}")
    subprocess.Popen(apps[app])


def close_app(app):
    speech.say(f"{ADDRESSING} {NICKNAME}, Closing {app}")
    subprocess.call(["taskkill", "/F", "/IM", f"{app}.exe"])


def main():
    open_app("chrome")


if __name__ == "__main__":
    main()
