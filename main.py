import sys
import time
import time_measure as timing
import RPi.GPIO as GPIO

reaction_time = timing.TimeMeasure()

# Setup GPIO inputs/outputs
    #Use Board pin numbering - etc. (12) in pinout command
GPIO.setmode(GPIO.BCM)
    #Setup GPIOs as inputs/outputs
GPIO.setup(27, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def input_callback(gpio_pin):  
    reaction_time.end_measure()
    GPIO.output(27,True)
    reaction_time.print_measure('Reaction time: ')


def main():
    GPIO.add_event_detect(21, GPIO.FALLING, callback = input_callback)

    while(1):
        time.sleep(2)
        reaction_time.start_measure()
        GPIO.output(27,False)

try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()



