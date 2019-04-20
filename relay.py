import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

input1=16

GPIO.setup(input1,GPIO.OUT)

while True:
    h=input("open or close")
    if h=="o":
        GPIO.output(input1,True)
        print("o")
    elif h=="c":
        GPIO.output(input1,False)
        print("c")
    else:
        print("h")
        
        

