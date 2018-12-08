import RPi.GPIO as GPIO
from time import sleep
import MySQLdb as sql
import os


GPIO.setwarnings(False)

port ={
        1:7,
        2:11,
        3:12,
        4:13,
        5:15,
        6:16,
        7:18,
        8:22,
        9:29,
        10:31,
        11:32,
        12:33,
        13:35,
        14:36,
        15:37,
        16:38
      }


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

GPIO.setup(32,GPIO.OUT)


def write(pin,value):
    GPIO.output(port[pin],GPIO.LOW)
