import time
import math
import threading;

from DRV8825 import DRV8825
from zMotor import zMotor
from rMotor import rMotor


from xController import XController;
from rzController import RZController;
from xrzController import XRZController;





if __name__ == "__main__":
 
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

    rMotorCur = rMotor(Motor1)
    zMotorCur = zMotor(Motor2)

    # Main loop
 
    xMotorCur = zMotorCur
    motorController = XRZController(xMotorCur,rMotorCur, zMotorCur)



