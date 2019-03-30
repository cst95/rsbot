import sys
sys.path.insert(0, './scripts')

from window import Window
from cursor import Cursor
from object_detector import ObjectDetector
from ore_miner_script import OreMinerScript


def main():
    runelite = Window('RumbIe')
    runelite.focus()
    runelite.resize(x=0,y=0,w=1000,h=700, absolute=True)
    cursor = Cursor()
    script = OreMinerScript('iron', runelite, cursor, 4)

    while True:
        script.botting_loop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
