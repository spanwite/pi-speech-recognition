from text_to_speech import say_text
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

def turn_on_light():
    say_text('Включаю')
    # GPIO.output(18, GPIO.HIGH)

def turn_off_light():
    say_text('Выключаю')
    # GPIO.output(18, GPIO.LOW)

light_control = [
    [turn_on_light, ('включи свет', "включи лампу")],
    [turn_off_light, ('выключи свет', "выключи лампу")]
]