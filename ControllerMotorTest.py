import RPi.GPIO as GPIO          
from time import sleep
from pyPS4Controller.controller import Controller


GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(12, 100)  # Initialize PWM on pwmPin 100Hz frequency    

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        print("UP!")
        pwm.start(50)
        
    def on_down_arrow_press(self):
        print("DOWN!")
        pwm.start(50)
        
    def on_up_down_arrow_release(self):
        print("STAHP!")
        pwm.stop()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)


