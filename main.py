from window import Window
from cursor import Cursor


def main():
    runelite = Window('RumbIe')
    runelite.focus()
    runelite.resize(x=100,y=100,w=800,h=500, absolute=True)
    cursor = Cursor()
    cursor.moveTo(*runelite.mid_point)

if __name__ == '__main__':
    main()
