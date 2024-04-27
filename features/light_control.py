import RPi.GPIO as GPIO
from time import sleep

class SmartLamp:
    def __init__(self, red_pin: int, green_pin: int, blue_pin: int):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)
        
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
    
    def __del__(self):
        GPIO.cleanup()

    def set_outputs(self, red_value: bool, green_value: bool, blue_value: bool):
        GPIO.output(self.red_pin, red_value)
        GPIO.output(self.green_pin, green_value)
        GPIO.output(self.blue_pin, blue_value)

    turn_off =   lambda self: self.set_outputs(GPIO.LOW,  GPIO.LOW,  GPIO.LOW)
    white =      lambda self: self.set_outputs(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)
    red =        lambda self: self.set_outputs(GPIO.HIGH, GPIO.LOW,  GPIO.LOW)
    green =      lambda self: self.set_outputs(GPIO.LOW,  GPIO.HIGH, GPIO.LOW)
    blue =       lambda self: self.set_outputs(GPIO.LOW,  GPIO.LOW,  GPIO.HIGH)
    purple =     lambda self: self.set_outputs(GPIO.HIGH, GPIO.LOW,  GPIO.HIGH)
    yellow =     lambda self: self.set_outputs(GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
    light_blue = lambda self: self.set_outputs(GPIO.LOW,  GPIO.HIGH, GPIO.HIGH)

    def show_colors(self):
        self.red()
        sleep(1)
        self.yellow()
        sleep(1)
        self.green()
        sleep(1)
        self.light_blue()
        sleep(1)
        self.blue()
        sleep(1)
        self.purple()
        sleep(1)
        self.white()
        sleep(1)
        self.turn_off()
    
lamp = SmartLamp(27, 22, 17)

light_control = [
    [lamp.red, 'цвет лампы красный'],
    [lamp.yellow, 'цвет лампы жёлтый'],
    [lamp.green, 'цвет лампы зелёный'],
    [lamp.light_blue, 'цвет лампы голубой'],
    [lamp.blue, 'цвет лампы синий'],
    [lamp.purple, 'цвет лампы фиолетовый'],
    [lamp.white, 'цвет лампы белый'],
    [lamp.turn_off, 'выключить лампу'],
    [lamp.show_colors, 'все цвета лампы']
]