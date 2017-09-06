"""Use keyboard to control Beo's wheels"""
import sys
import readchar
from Wheels import Wheels

WHEELS = Wheels()

def read_char():
    """Detects key strokes"""
    key_stroke = str(repr(readchar.readkey()))
    key_stroke = key_stroke.replace("'", "")
    if key_stroke == "\\x1b[A":
        return "up"
    elif key_stroke == "\\x1b[C":
        return "right"
    elif key_stroke == "\\x1b[D":
        return "left"
    elif key_stroke == "\\x1b[B":
        return "down"
    elif key_stroke == " ":
        return "space"
    elif key_stroke == "\\x03":
        return "ctrlC"

while True:
    KEY_READ = read_char()
    if KEY_READ == "ctrlC":
        WHEELS.move_wheel_left(0)
        WHEELS.move_wheel_right(0)
        sys.exit(1)
    elif KEY_READ == "up":
        WHEELS.move_wheel_left(2)
        WHEELS.move_wheel_right(2)
    elif KEY_READ == "right":
        WHEELS.move_wheel_left(1)
        WHEELS.move_wheel_right(-1)
    elif KEY_READ == "left":
        WHEELS.move_wheel_left(-1)
        WHEELS.move_wheel_right(1)
    elif KEY_READ == "down":
        WHEELS.move_wheel_left(-2)
        WHEELS.move_wheel_right(-2)
    elif KEY_READ == "space":
        WHEELS.move_wheel_left(0)
        WHEELS.move_wheel_right(0)
