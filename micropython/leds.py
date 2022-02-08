from machine import Pin, PWM
import uasyncio

led_red = PWM(Pin(0))
led_green = PWM(Pin(2))
led_blue = PWM(Pin(15))



#led_pin_blue = 2
#led_blue = Pin(2, Pin.OUT)

async def blink():
    led_red.duty(0)
    led_green.duty(0)
    led_blue.duty(0)
    red = 0
    blue = 0
    while True:
        red = not red
        if red:
            led_red.duty(1023)
        else:
            led_red.duty(0)
        #v = not led_blue.value()
        #led_blue.value(v)
        await uasyncio.sleep_ms(1000)
        blue = not blue
        if blue:
            led_blue.duty(1023)
        else:
            led_blue.duty(0)
        await uasyncio.sleep_ms(3000)

def test():
    loop = uasyncio.get_event_loop()
    loop.create_task(blink())
    loop.run_forever()

if __name__ == '__main__':
    test()
    