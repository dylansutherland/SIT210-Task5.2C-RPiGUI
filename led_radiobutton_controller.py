from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware Definitions
greenLed = LED(14)
blueLed = LED(15)
redLed = LED(18)

## GUI Definitions
win = Tk()
win.title("LED Controller")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event Functions
def greenLedToggle():
    blueLed.off()
    redLed.off()
    greenLed.on()

def blueLedToggle():
    redLed.off()
    greenLed.off()
    blueLed.on()

def redLedToggle():
    blueLed.off()
    greenLed.off()
    redLed.on()

def onToggle():
    redLed.on()
    blueLed.on()
    greenLed.on()

def offToggle():
    redLed.off()
    blueLed.off()
    greenLed.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## Widgets
Label(win, width = 20, text = 'Select an LED to turn on: ').grid(row = 0, column = 1)
selectedLed = StringVar()

redLedButton = Radiobutton(win, text = 'Red', font = myFont, variable = selectedLed, value = 'red', command = redLedToggle, height = 1, width = 27)
redLedButton.grid(row = 1, column = 1)

blueLedButton = Radiobutton(win, text = 'Blue', font = myFont, variable = selectedLed, value = 'blue', command = blueLedToggle, height = 1, width = 27)
blueLedButton.grid(row = 2, column = 1)

greenLedButton = Radiobutton(win, text = 'Green', font = myFont, variable = selectedLed, value = 'green', command = greenLedToggle, height = 1, width = 27)
greenLedButton.grid(row = 3, column = 1)

allOnButton = Radiobutton(win, text = 'All On', font = myFont, variable = selectedLed, value = 'off', command = onToggle, height = 1, width = 27)
allOnButton.grid(row = 4, column = 1)

allOffButton = Radiobutton(win, text = 'All Off', font = myFont, variable = selectedLed, value = 'on', command = offToggle, height = 1, width = 24)
allOffButton.grid(row = 5, column = 1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 24)
exitButton.grid(row = 6, column = 1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
