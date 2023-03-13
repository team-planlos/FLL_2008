#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ML = Motor(Port.C)
MR = Motor(Port.B)
MM = Motor(Port.A)

#SL = ColorSensor(Port.)
#SR = ColorSensor(Port.)

# Write your program here.
ev3.speaker.beep()

MR.run(100)
ML.run(-100)
wait(2000)
MR.stop()
ML.stop()

MM.run(1000)
wait(1000)
MM.stop()

ev3.speaker.beep()
wait(100)
ev3.speaker.beep()