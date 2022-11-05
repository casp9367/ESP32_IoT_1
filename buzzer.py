from machine import Pin
from machine import PWM
from time import sleep
import _thread

B_PIN = 26

buzzer = PWM(Pin(B_PIN, Pin.OUT))


def buz_lyd():
    while True:
        buzzer.duty(512)
        buzzer.freq(1300)
        sleep(0.4)
        buzzer.duty(0)
        sleep(600)
        
_thread.start_new_thread(buz_lyd,())
