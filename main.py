import argparse
import time
import webbrowser


DEFAULT_URL = "https://www.youtube.com/watch?v=D7ab595h0AU"

"""
Very low intervals may lead to unintended consequences like crashing/freezing/etc.
Prevent the interval from going below this value (in seconds). Change at your own risk!
"""
SPAM_THRESHOLD = 10


def take_a_break(interval_in_seconds, url, verbose):
    while True:
        for t in range(int(interval_in_seconds)):
            time.sleep(1)
            if(verbose):
                print("Time left:", int(interval_in_seconds - t), "s", end="\r")
        webbrowser.open_new(url)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("interval", type=float, help="Disturb me after this much time (in seconds by default)")
    parser.add_argument("url", nargs="?", default=DEFAULT_URL, help="I like this url (open this in the browser)")
    parser.add_argument("-v", "--verbose", action="store_true", help="I can't take this, I need to see how much time is left")
    
    units = parser.add_mutually_exclusive_group()
    units.add_argument("-m", "--minutes", action="store_true", help="Seconds? I want minutes!")
    units.add_argument("-H", "--hours", action="store_true", help="Minutes? Pfft! Hours, or nothing")

    args = parser.parse_args()
    interval_in_seconds = args.interval

    if interval_in_seconds < 0:
        raise ValueError("Negative interval not allowed. I don't have a time machine, you know.")

    if args.minutes:
        interval_in_seconds *= 60
    elif args.hours:
        interval_in_seconds *= 3600

    if interval_in_seconds < SPAM_THRESHOLD:
        raise ValueError("This interval seems too low, and may cause crashes/freezes/etc.")

    try:
        take_a_break(interval_in_seconds, args.url, args.verbose)
    except KeyboardInterrupt:
        print("Thanks for trying this! Good night/day/whatever.")


if __name__ == "__main__":
    main()
