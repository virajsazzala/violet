#!/usr/bin/env python3

import src.calendar.date_time as date_time
import src.calendar.reminder as reminders
import re

import src.apps.access_apps as access_apps
import src.browser.access_sites as access_sites
import src.senses.speech as speech
from src.consts import ADDRESSING, NICKNAME, SLEEP_CALL, WAKE_UP_CALL
import src.music.spotify as spotify


def main():
    while True:
        text = speech.listen()
        # everytime "hey violet" is said, it will listen for the next command
        if re.search(WAKE_UP_CALL, text):

            # if "go to sleep now" is found in text, break the loop
            if re.search(SLEEP_CALL, text):
                speech.say(f"{ADDRESSING} {NICKNAME}, night night!")
                break

            # TODO: do a re.search() for specific set of keywords rather than sentences
            # if "open" is found in text, search for the website
            words = ("open", "on chrome")
            if all([re.search(w, text) for w in words]):
                access_sites.search_online(text)

            words = ("open", "application")
            if all([re.search(w, text) for w in words]):
                # get the app name from the text
                app = text.split("application")[1][:-1].strip()
                access_apps.open_app(app)

            words = ("close", "application")
            if all([re.search(w, text) for w in words]):
                # get the app name from the text
                app = text.split("application")[1][:-1].strip()
                access_apps.close_app(app)

            # if "time right now" is found in text, tell the time
            words = ("time", "now")
            if all([re.search(w, text) for w in words]):
                date_time.get_time()

            # if "today's date" is found in text, tell the date
            if re.search("today's date", text):
                date_time.get_date()

            # if "set a reminder" is found in text, set a reminder
            words = ("remind me", "to")
            if all([re.search(w, text) for w in words]):
                reminders.prompt(text)

            # if "show my reminders" is found in text, show reminders
            words = ("put", "reminders", "screen")
            if all([re.search(w, text) for w in words]):
                reminders.display_reminders()

            # if "what are my reminders" is found in text, say reminders
            words = ("what", "reminders")
            if all([re.search(w, text) for w in words]):
                reminders.say_reminders()

            # if "delete reminder" is found in text, delete reminder
            words = ("delete", "reminder")
            if all([re.search(w, text) for w in words]):
                # TODO: open a dialogue box to check the reminder to be deleted
                reminder = (text.split("reminder")[1].strip())[:-1]
                reminders.delete_reminder(reminder)

            # if "download song" is found in text, prompt to download song
            words = ("download", "song")
            if all([re.search(w, text) for w in words]):
                spotify.prompt()


if __name__ == "__main__":
    main()
