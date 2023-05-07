import csv
import re
import time
import tkinter as tk
from datetime import date
from tkinter import ttk

import src.senses.speech as speech
from src.consts import REMINDERS_FILE, REMINDERS_TEMP_FILE


def prompt(text):
    # get the time and reminder from the text, time comes after the word at
    reminder = (text.split("remind me")[1].strip())[:-1]
    if re.search("at", reminder):
        time = reminder.split("at")[1].strip()
        reminder = reminder.split("at")[0].strip()
        set_reminder(time, reminder)
        speech.say(f"Reminder set! {reminder} at {time}")
    else:
        set_reminder("None", reminder)
        speech.say(f"Reminder set! {reminder}")


# works with text
def set_reminder(rem_time, rem):
    with open(REMINDERS_FILE, 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([rem_time, rem, date.today()])


def get_reminders():
    with open(REMINDERS_FILE, 'r') as f:
        reader = csv.reader(f)
        return list(reader)[1:]


def display_reminders():
    window = tk.Tk()
    window.geometry("500x400")
    window.title("Reminders")
    reminders = get_reminders()
    if len(reminders) == 1:
        print("You have no reminders set")
        speech.say("You have no reminders set")
    else:
        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=30, width=30)
        treeview = ttk.Treeview(window, columns=("time", "reminder"), show="headings")
        treeview.heading("time", text="Time")
        treeview.heading("reminder", text="Reminder")
        for reminder in reminders[1:]:
            treeview.insert("", tk.END, values=(reminder[0], reminder[1]))

        treeview.pack(padx=20, pady=20)
        window.mainloop()


# works with speech
def say_reminders():
    reminders = get_reminders()
    print(len(reminders))
    if len(reminders) == 1:
        speech.say("You have no reminders set")
    else:
        for reminder in reminders[1:]:
            speech.say(f"{reminder[1]} by {reminder[0]}")
            time.sleep(0.2)


def delete_reminder(reminder):
    reminders = get_reminders()
    print(len(reminders))
    if len(reminders) == 1:
        speech.say("You have no reminders set")
        return

    with open(REMINDERS_FILE, 'r', newline='') as firstfile, open(REMINDERS_TEMP_FILE, 'w', newline='') as secondfile:
        for line in firstfile:
            secondfile.write(line)

    with open(REMINDERS_TEMP_FILE, 'r', newline='') as inp, open(REMINDERS_FILE, 'w', newline='') as out:
        writer = csv.writer(out)
        rems = csv.reader(inp)
        for row in rems:
            if row[1] == reminder:
                speech.say("Removed reminder!")
                continue
            if row[1] != reminder:
                writer.writerow(row)


def main():
    pass


if __name__ == "__main__":
    display_reminders()
