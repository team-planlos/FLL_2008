#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import threading

help(threading)


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ML = Motor(Port.C)
MR = Motor(Port.B)
MM = Motor(Port.A)

SL = ColorSensor(Port.S2)
SR = ColorSensor(Port.S3)


db = DriveBase(ML, MR, 88, 88)

# Write your program here.
ev3.speaker.beep()

db.settings(200, 200, 200, 200)

db.straight(100)
db.turn(-47)

db.drive(200,0)
wait(3000)
while SL.color() != Color.RED:
    wait(50)
db.stop()
db.turn(30)
db.straight(100)
wait(1000)
db.turn(110)
db.straight(500)

wait (5000)

ev3.speaker.beep()
wait(100)
ev3.speaker.beep()
