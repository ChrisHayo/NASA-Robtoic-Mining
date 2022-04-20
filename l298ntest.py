import RPi.GPIO as GPIO          
from time import sleep
from pyPS4Controller.controller import Controller
from subprocess import call


in_fla_1 = 24 # front linear actuator retraction
in_fla_2 = 23 # front linear actuator extension
in_bla_1 = 14 # back linear actuator retraction
in_bla_2 = 15 # back linear actuator retraction
in_lm_1 = 8   # left side motors forward
in_lm_2 = 7   # left side motors backward
in_rm_1 = 2   # right side motors forward
in_rm_2 = 3   # right side motors backward
in_ls_1 = 17  # lead screw channel A+
in_ls_2 = 27  # lead screw channel A-
in_ls_3 = 22  # lead screw channel B+
in_ls_4 = 10  # lead screw channel B-
in_em_1 = 11   # excavation motor forward
in_em_2 = 9  # excavation motor backward

en_motor = 12 # enable pin used for controlling speed of drive motors
en_leadscrew = 13 # enable pin used for controlling speed of lead screw

GPIO.setmode(GPIO.BCM) # setting mode of GPIO pins to be defined by the GPIO number

# setting all GPIO pins as outputs
GPIO.setup(in_fla_1,GPIO.OUT)
GPIO.setup(in_fla_2,GPIO.OUT)
GPIO.setup(in_bla_1,GPIO.OUT)
GPIO.setup(in_bla_2,GPIO.OUT)
GPIO.setup(in_lm_1,GPIO.OUT)
GPIO.setup(in_lm_2,GPIO.OUT)
GPIO.setup(in_rm_1,GPIO.OUT)
GPIO.setup(in_rm_2,GPIO.OUT)
GPIO.setup(in_ls_1,GPIO.OUT)
GPIO.setup(in_ls_2,GPIO.OUT)
GPIO.setup(in_ls_3,GPIO.OUT)
GPIO.setup(in_ls_4,GPIO.OUT)
GPIO.setup(in_em_1,GPIO.OUT)
GPIO.setup(in_em_2,GPIO.OUT)
GPIO.setup(en_motor,GPIO.OUT)
GPIO.setup(en_leadscrew,GPIO.OUT)

# initialising the pins as LOW (off)
GPIO.output(in_fla_1,GPIO.LOW)
GPIO.output(in_fla_2,GPIO.LOW)
GPIO.output(in_bla_1,GPIO.LOW)
GPIO.output(in_bla_2,GPIO.LOW)
GPIO.output(in_lm_1,GPIO.LOW)
GPIO.output(in_lm_2,GPIO.LOW)
GPIO.output(in_rm_1,GPIO.LOW)
GPIO.output(in_rm_2,GPIO.LOW)
GPIO.output(in_ls_1,GPIO.LOW)
GPIO.output(in_ls_2,GPIO.LOW)
GPIO.output(in_ls_3,GPIO.LOW)
GPIO.output(in_ls_4,GPIO.LOW)
GPIO.output(in_em_1,GPIO.LOW)
GPIO.output(in_em_2,GPIO.LOW)

def cleanup():
    GPIO.output(in_fla_1,GPIO.LOW)
    GPIO.output(in_fla_2,GPIO.LOW)
    GPIO.output(in_bla_1,GPIO.LOW)
    GPIO.output(in_bla_2,GPIO.LOW)
    GPIO.output(in_lm_1,GPIO.LOW)
    GPIO.output(in_lm_2,GPIO.LOW)
    GPIO.output(in_rm_1,GPIO.LOW)
    GPIO.output(in_rm_2,GPIO.LOW)
    GPIO.output(in_ls_1,GPIO.LOW)
    GPIO.output(in_ls_2,GPIO.LOW)
    GPIO.output(in_ls_3,GPIO.LOW)
    GPIO.output(in_ls_4,GPIO.LOW)
    GPIO.output(in_em_1,GPIO.LOW)
    GPIO.output(in_em_2,GPIO.LOW)
    GPIO.cleanup()
    
p_motor = GPIO.PWM(en_motor,500) 
p_leadsrew = GPIO.PWM(en_leadscrew,500)

p_motor.start(50)


accl = [25,50,75,100] # vector to vary acceleration speeds
step_sleep = 0.002
step_count = 200

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        # for loop to accelerate
        for i in accl:
            p_motor.ChangeDutyCycle(i)
            GPIO.output(in_lm_1,GPIO.HIGH)
            GPIO.output(in_lm_2,GPIO.LOW)
            GPIO.output(in_rm_1,GPIO.HIGH)
            GPIO.output(in_rm_2,GPIO.LOW)
            sleep(0.3)
        # continue spinning motors
        GPIO.output(in_lm_1,GPIO.HIGH)
        GPIO.output(in_lm_2,GPIO.LOW)
        GPIO.output(in_rm_1,GPIO.HIGH)
        GPIO.output(in_rm_2,GPIO.LOW)
        
    def on_down_arrow_press(self):
        # for loop to accelerate
        for i in accl:
            p_motor.ChangeDutyCycle(i)
            GPIO.output(in_lm_1,GPIO.LOW)
            GPIO.output(in_lm_2,GPIO.HIGH)
            GPIO.output(in_rm_1,GPIO.LOW)
            GPIO.output(in_rm_2,GPIO.HIGH)
            sleep(0.3)
        # continue spinning motors
        GPIO.output(in_lm_1,GPIO.LOW)
        GPIO.output(in_lm_2,GPIO.HIGH)
        GPIO.output(in_rm_1,GPIO.LOW)
        GPIO.output(in_rm_2,GPIO.HIGH)

    def on_up_down_arrow_release(self):
        GPIO.output(in_lm_1,GPIO.LOW)
        GPIO.output(in_lm_2,GPIO.LOW)
        GPIO.output(in_rm_1,GPIO.LOW)
        GPIO.output(in_rm_2,GPIO.LOW)
        
    def on_left_arrow_press(self):
        # for loop to accelerate
        for i in accl:
            p_motor.ChangeDutyCycle(i)
            GPIO.output(in_lm_1,GPIO.LOW)
            GPIO.output(in_lm_2,GPIO.HIGH)
            GPIO.output(in_rm_1,GPIO.HIGH)
            GPIO.output(in_rm_2,GPIO.LOW)
            sleep(0.3)
        # continue spinning motors
        GPIO.output(in_lm_1,GPIO.LOW)
        GPIO.output(in_lm_2,GPIO.HIGH)
        GPIO.output(in_rm_1,GPIO.HIGH)
        GPIO.output(in_rm_2,GPIO.LOW)
            
    def on_right_arrow_press(self):
        # for loop to accelerate
        for i in accl:
            p_motor.ChangeDutyCycle(i)
            GPIO.output(in_lm_1,GPIO.HIGH)
            GPIO.output(in_lm_2,GPIO.LOW)
            GPIO.output(in_rm_1,GPIO.LOW)
            GPIO.output(in_rm_2,GPIO.HIGH)
            sleep(0.3)
        # continue spinning motors
        GPIO.output(in_lm_1,GPIO.HIGH)
        GPIO.output(in_lm_2,GPIO.LOW)
        GPIO.output(in_rm_1,GPIO.LOW)
        GPIO.output(in_rm_2,GPIO.HIGH)
            
    def on_left_right_arrow_release(self):
        GPIO.output(in_lm_1,GPIO.LOW)
        GPIO.output(in_lm_2,GPIO.LOW)
        GPIO.output(in_rm_1,GPIO.LOW)
        GPIO.output(in_rm_2,GPIO.LOW)
        
    def on_x_press(self):
        p_motor.ChangeDutyCycle(100)
        GPIO.output(in_em_1,GPIO.HIGH)
        GPIO.output(in_em_2,GPIO.LOW)
        
    def on_square_press(self):
        GPIO.output(in_em_1,GPIO.LOW)
        GPIO.output(in_em_2,GPIO.LOW)
        
    def on_triangle_press(self):
        p_motor.ChangeDutyCycle(100)
        GPIO.output(in_fla_1,GPIO.HIGH)
        GPIO.output(in_fla_2,GPIO.LOW)
        
    def on_triangle_release(self):
        GPIO.output(in_fla_1,GPIO.LOW)
        GPIO.output(in_fla_2,GPIO.LOW)
        
    def on_circle_press(self):
        p_motor.ChangeDutyCycle(100)
        GPIO.output(in_fla_1,GPIO.LOW)
        GPIO.output(in_fla_2,GPIO.HIGH)
        
    def on_circle_release(self):
        GPIO.output(in_fla_1,GPIO.LOW)
        GPIO.output(in_fla_2,GPIO.LOW)
        
    def on_R1_press(self):
        p_motor.ChangeDutyCycle(100)
        GPIO.output(in_bla_1,GPIO.HIGH)
        GPIO.output(in_bla_2,GPIO.LOW)
        
    def on_R1_release(self):
        GPIO.output(in_bla_1,GPIO.LOW)
        GPIO.output(in_bla_2,GPIO.LOW)
        
    def on_L1_press(self):
        p_motor.ChangeDutyCycle(100)
        GPIO.output(in_bla_1,GPIO.LOW)
        GPIO.output(in_bla_2,GPIO.HIGH)
        
    def on_L1_release(self):
        GPIO.output(in_bla_1,GPIO.LOW)
        GPIO.output(in_bla_2,GPIO.LOW)
        
    def on_L3_press(self):
        i = 0
        for i in range(step_count):
            if i%4==0:
                GPIO.output(in_ls_4,GPIO.HIGH)
                GPIO.output(in_ls_3,GPIO.LOW)
                GPIO.output(in_ls_2,GPIO.LOW)
                GPIO.output(in_ls_1,GPIO.LOW)
            elif i%4==1:
                GPIO.output(in_ls_4,GPIO.LOW)
                GPIO.output(in_ls_3,GPIO.LOW)
                GPIO.output(in_ls_2,GPIO.HIGH)
                GPIO.output(in_ls_1,GPIO.LOW)
            elif i%4==2:
                GPIO.output(in_ls_4,GPIO.LOW)
                GPIO.output(in_ls_3,GPIO.HIGH)
                GPIO.output(in_ls_2,GPIO.LOW)
                GPIO.output(in_ls_1,GPIO.LOW)
            elif i%4==3:
                GPIO.output(in_ls_4,GPIO.LOW)
                GPIO.output(in_ls_3,GPIO.LOW)
                GPIO.output(in_ls_2,GPIO.LOW)
                GPIO.output(in_ls_1,GPIO.HIGH)
     
            sleep(step_sleep)
    def on_playstation_button_press(self):
        quit()
        
    def on_options_press(self):     
        call("sudo shutdown -h now", shell=True)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=120)

