# display an image on Pingie Pie, scrolling it downwards
# kudos to lutoma for the original code

import base64
import time
import json
import requests
import sys

from bitarray import bitarray  # pip install bitarray

COLS = 152
ROWS = 16


def send_frame(data):
    data = base64.b64encode(data.tobytes())
    payload = json.dumps({'pixmap': data.decode('ascii')})
    req = requests.post('http://pingiepie.rzl:8000', data = payload)

    print(req)


def main():
    with open(sys.argv[1]) as img:
        [next(img) for _ in range(3)]

        raw = img.read() + ROWS*COLS*'0'
        pbm = ''.join(filter(lambda char: char in ('0', '1'), raw))

        n = 0
        while NotImplemented:
            img_array = bitarray(pbm[n:n+(ROWS * COLS)])
            n = (n + COLS) % (len(pbm) - COLS * ROWS)
            print(n)
            send_frame(img_array)


if __name__ == "__main__":
    main()
