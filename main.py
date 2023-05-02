
#!/usr/bin/env python3

import src.calendar.date_time as date_time
import src.calendar.reminder as reminders
import re

import src.apps.access_apps as access_apps
import src.browser.access_sites as access_sites
import src.senses.speech as speech
from src.consts import ADDRESSING, NICKNAME, SLEEP_CALL, WAKE_UP_CALL


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
            if re.search("open on chrome", text):
                access_sites.search_online(text)

            if re.search("open the application", text):
                # get the app name from the text
                app = text.split("open the application")[1][:-1].strip()
                access_apps.open_app(app)

            if re.search("close the application", text):
                # get the app name from the text
                app = text.split("close the application")[1][:-1].strip()
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
                # get the time and reminder from the text, time comes after the word at
                reminder = (text.split("remind me")[1].strip())[:-1]
                if re.search("at", reminder):
                    time = reminder.split("at")[1].strip()
                    reminder = reminder.split("at")[0].strip()
                    reminders.set_reminder(time, reminder)
                    speech.say(f"Reminder set! {reminder} at {time}")
                else:
                    reminders.set_reminder("None", reminder)
                    speech.say(f"Reminder set! {reminder}")

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


if __name__ == "__main__":
    main()
