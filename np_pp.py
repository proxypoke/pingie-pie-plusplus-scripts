#!/usr/bin/env python3
# display the currently playing song from mpd on Pingie Pie++

import time

import requests  # pip install requests
import sh        # pip install sh


MPD_HOST = "mpd.rzl"
SCROLL_WIDTH = 20


def current():
    return str(sh.mpc("current", "--host", MPD_HOST, '-f',
                      '"%title%" by "%artist%" from "%album%"'))


def update(text):
    requests.get("http://pingiepie.rzl:8000/{0}".format(text))


def scroll(text):
    text += ' ' * 10
    n = 0
    while NotImplemented:
        text = text[1:] + text[0]
        #yield text[n:n + SCROLL_WIDTH]
        yield text
        n = (n + 1) % len(text)


def main():
    while NotImplemented:
        song = current()
        for line in scroll(song):
            if song != current():
                break
            update(line)
            time.sleep(0.1)


if __name__ == "__main__":
    main()
