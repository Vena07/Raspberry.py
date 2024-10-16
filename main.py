import machine
import time


led1 = machine.Pin(1,machine.Pin.OUT)
led2 = machine.Pin(2,machine.Pin.OUT)
led3 = machine.Pin(3,machine.Pin.OUT)
led4 = machine.Pin(4,machine.Pin.OUT)

ledA = 0
ledB = 0
ledC = 0
ledD = 0
vybrano = True
rada = 1
while True:
    for i in range(2):
        time.sleep(1)
        if rada == 1:
            led4.value(0)
            led1.value(1)
            rada = 2
        elif rada == 2:
            led1.value(0)
            led2.value(1)
            rada = 3
        elif rada == 3:
            led2.value(0)
            led3.value(1)
            rada = 4
        elif rada == 4:
            led3.value(0)
            led4.value(1)
            rada = 1
    for i in range(20):
        time.sleep(0.1)
        if rada == 1:
            led4.value(0)
            led1.value(1)
            rada = 2
        elif rada == 2:
            led1.value(0)
            led2.value(1)
            rada = 3
        elif rada == 3:
            led2.value(0)
            led3.value(1)
            rada = 4
        elif rada == 4:
            led3.value(0)
            led4.value(1)
            rada = 1
    for i in range(20):
        time.sleep(0.05)
        if rada == 1:
            led4.value(0)
            led1.value(1)
            rada = 2
        elif rada == 2:
            led1.value(0)
            led2.value(1)
            rada = 3
        elif rada == 3:
            led2.value(0)
            led3.value(1)
            rada = 4
        elif rada == 4:
            led3.value(0)
            led4.value(1)
            rada = 1
    for i in range(20):
        time.sleep(0.1)
        if rada == 1:
            led4.value(0)
            led1.value(1)
            rada = 2
        elif rada == 2:
            led1.value(0)
            led2.value(1)
            rada = 3
        elif rada == 3:
            led2.value(0)
            led3.value(1)
            rada = 4
        elif rada == 4:
            led3.value(0)
            led4.value(1)
            rada = 1
    for i in range(2):
        time.sleep(1)
        if rada == 1:
            led4.value(0)
            led1.value(1)
            rada = 2
        elif rada == 2:
            led1.value(0)
            led2.value(1)
            rada = 3
        elif rada == 3:
            led2.value(0)
            led3.value(1)
            rada = 4
        elif rada == 4:
            led3.value(0)
            led4.value(1)
            rada = 1


while False:
    while vybrano == True:
        vyber = int(input("vyberte si : 1 / 2/ 3/ 4 :") )
        if 0< vyber <5:
            vybrano = False
        else:
            print("Špatný výbeětr")
            print()
    vybrano = True
    if vyber == 1:
        if ledA == 0:
            ledA = 1
        else:
            ledA = 0
    
    elif vyber == 2:
        if ledB == 0:
            ledB = 1
        else:
            ledB = 0
    
    elif vyber == 3:
        if ledC == 0:
            ledC = 1
        else:
            ledC = 0
    
    elif vyber == 4:
        if ledD == 0:
            ledD = 1
        else:
            ledD = 0
    
    
    
    
    
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)