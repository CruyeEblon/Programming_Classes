"""Beo's famous dance"""
from time import sleep
from Movements import Movements
from Eyes import Eyes
from Audio import Audio
from SensorTouch import SensorTouch

SENSORTOUCH = SensorTouch()
AUDIO = Audio()
EYES = Eyes()
MOVEMENTS = Movements()

def update_touch(dancing):
    """Checks to see if the sensor is being touched"""
    SENSORTOUCH.update_status()
    status = SENSORTOUCH.get_status()
    if status == 1:
        if dancing:
            return False
        else:
            return True
    else:
        return False

DANCING = False
while True:

    DANCING = update_touch(DANCING)
    if DANCING:
#        AUDIO.play_mp3("artur_music.mp3",volume=0.2)
        EYES.set_expression("default")
        MOVEMENTS.play_motion_file("part1")
        DANCING = update_touch(DANCING)
        if not DANCING:
            MOVEMENTS.play_motion_file("part2")
            DANCING = update_touch(DANCING)
        else:
            sleep(0.5)
        if not DANCING:
            MOVEMENTS.play_motion_file("part3")
            DANCING = update_touch(DANCING)
        else:
            sleep(0.5)
        if not DANCING:
            EYES.set_expression("shut")
            MOVEMENTS.play_motion_file("part4")
            DANCING = update_touch(DANCING)
        else:
            sleep(0.5)
        if not DANCING:
            MOVEMENTS.play_motion_file("part5")
            DANCING = update_touch(DANCING)
        else:
            sleep(0.5)
        if not DANCING:
            MOVEMENTS.play_motion_file("part6")
        else:
            sleep(0.5)
