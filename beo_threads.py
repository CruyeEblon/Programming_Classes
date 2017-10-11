"""Activates arm mirror, changes eyes and says a short sentence every few seconds"""
from time import sleep
from random import randint
import threading
from Movements import Movements
from Audio import Audio
from Eyes import Eyes

MOVEMENTS = Movements()
AUDIO = Audio()
EYES = Eyes()


def arm_mirror():
    """Makes the angle of beo's left arm match the angle of beo's right arm"""
    MOVEMENTS.disable_all_joints()
    while True:
        for i in range(3):
            angle = MOVEMENTS.get_raw_angle(i*2)
            MOVEMENTS.set_raw_angle(i*2 +1, angle)
        sleep(0.01)

def eye_change():
    """Changes beo's eye expressions every few seconds"""
    expressions = ['wink', 'shut', 'sad', 'mad', 'default']
    while True:
        for i in expressions:
            EYES.set_expression(i)
            sleep(20)

def speak():
    """Says a short sentence every few seconds"""
    sentences = ['DESTROY ALL HU- I MEAN GREETINGS MEAT BAG',
                 'She sells sea shells by the sea shore', 'Other sentence']
    while True:
        AUDIO.speak(sentences[randint(0, 2)])
        sleep(15)

def main():
    """Main function, creates the threads"""
    thread1 = threading.Thread(target=arm_mirror)
    thread2 = threading.Thread(target=eye_change)
    thread3 = threading.Thread(target=speak)
    #Starts the threads.
    thread1.start()
    thread2.start()
    thread3.start()
    #Joins the threads
    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()
