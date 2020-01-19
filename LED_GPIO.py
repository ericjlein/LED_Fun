from gpiozero import LED
from time import sleep

led00 = LED(2)
led01 = LED(3)
led02 = LED(4)
led03 = LED(17)
led04 = LED(27)
led05 = LED(22)
led06 = LED(10)
led07 = LED(9)
led08 = LED(11)
led09 = LED(14)
led10 = LED(15)
led11 = LED(18)
led12 = LED(23)
led13 = LED(24)
led14 = LED(25)
led15 = LED(8)
led16 = LED(7)

leds = [
    led00,
    led01,
    led02,
    led03,
    led04,
    led05,
    led06,
    led07,
    led08,
    led09,
    led10,
    led11,
    led12,
    led13,
    led14,
    led15,
    led16
    ]


led01.off()
sleep(.5)


for led in leds:
    led.on()
    sleep(.035)

sleep(2)

for led in reversed(leds):
    led.off()
    sleep(.035)

sleep(2)

def blink(leds):
    i = 0
    l = leds[8]
    y = 0.01
    x = 0

    while i < 1e4:
        helpMe = False

        for led in leds:

            led.on()

            if led == l:
                leds[(leds.index(led) - 8) % 17].on()
                l = leds[(leds.index(led) + 8)  % 16]
                helpMe = True

            def getShitDone(leds):
                leds[(leds.index(led) - 8) % 17].on()
                helpMe = False


            if helpMe:
                getShitDone(leds)

            sleep(y)
            led.off()
            leds[(leds.index(led) - 8) % 17].off()


        def slower(y):
            y *= 1.01
            print('slower')
            return y

        def faster(y):
            y /= 1.01
            print('faster')
            return y

        if x < 0.1:
            y = slower(y)
        elif x == 0.1:
            print('REVERSED')
            leds.reverse()
        elif x > 0.1:
            y = faster(y)
        elif x == 0.2:
            break

        x += 0.001
        x = round(x, 4)
        #print(x)
        i += 1



blink(leds)
