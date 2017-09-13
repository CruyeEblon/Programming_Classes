"""Converts between units of distance measuring"""
import sys
import readchar

def read_char():
    """Detects key strokes"""
    key_stroke = str(repr(readchar.readkey()))
    key_stroke = key_stroke.replace("'", "")
    if key_stroke == "1":
        return "meters_to_feet"
    elif key_stroke == "2":
        return "feet_to_meters"
    elif key_stroke == "\\x03":
        sys.exit(1)
METERS_TO_FEET = lambda x: x*3.28084
FEET_TO_METERS = lambda x: x/3.28084

while True:
    print("Press 1 to convert meters to feet, press 2 to convert feet to meters")
    CHARINPUT = read_char()
    NUMBER = raw_input("Please enter the number: ")
    if CHARINPUT == "meters_to_feet":
        print(METERS_TO_FEET(int(NUMBER)))
    elif CHARINPUT == "feet_to_meters":
        print(FEET_TO_METERS(int(NUMBER)))
