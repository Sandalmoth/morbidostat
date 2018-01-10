#!/usr/bin/python3


from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import time


def main():
    bd = PyMata3()

    bd.set_pin_mode(2, Constants.OUTPUT)

    for i in range(100):
        bd.digital_write(2, 1)
        print('  1')
        time.sleep(3)
        bd.digital_write(2, 0)
        print('0  ')
        time.sleep(2)

    bd.shutdown()


if __name__ == "__main__":
    main()
