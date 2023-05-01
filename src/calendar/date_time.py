from datetime import date, datetime

import src.senses.speech as speech


def get_date():
    speech.say(f"Today's date is {date.today().strftime('%A %d %B %Y')}")


def get_time():
    def get_part_of_day(hour):
        return (
            "morning"
            if 5 <= hour <= 11
            else "afternoon"
            if 12 <= hour <= 17
            else "evening"
            if 18 <= hour <= 22
            else "night"
        )

    now = datetime.now()
    current_time = now.strftime('%H:%M')
    speech.say(f"It's currently {current_time} in the {get_part_of_day(now.hour)}!")


def main():
    get_date()
    get_time()


if __name__ == '__main__':
    main()
