import RPi.GPIO as GPIO
import threading
import time
import random


# Push Button class with debouncing
# Usage:
# cb = ButtonHandler(pin, real_cb, edge='rising', bouncetime=100)
# cb.start()
# GPIO.add_event_detect(pin, GPIO.RISING, callback=cb)
class ButtonHandler(threading.Thread):
    def __init__(self, pin, func, edge='both', bouncetime=200):
        super().__init__(daemon=True)
        self.edge = edge
        self.func = func
        self.pin = pin
        self.bouncetime = float(bouncetime)/1000
        self.lastpinval = GPIO.input(self.pin)
        self.lock = threading.Lock()

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def __call__(self, *args):
        if not self.lock.acquire(blocking=False):
            return
        t = threading.Timer(self.bouncetime, self.read, args=args)
        t.start()

    def read(self, *args):
        pinval = GPIO.input(self.pin)
        if (
                ((pinval == 0 and self.lastpinval == 1) and
                 (self.edge in ['falling', 'both'])) or
                ((pinval == 1 and self.lastpinval == 0) and
                 (self.edge in ['rising', 'both']))
        ):
            self.func(*args)

        self.lastpinval = pinval
        self.lock.release()


# RGB LED class with Pulse Width Modulation (PWM)
# Usage: led1 = RGBLED([3, 5, 7])
class RGBLED:
    def __init__(self, pins):
        if len(pins) is not 3:
            sys.exit(
                "RGBLED: Constructor must be called with length-3 array of pin numbers")

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        self.pins = pins

    def set_next_pin(self):
        next_pin = self.pins[random.randint(0, 2)]
        GPIO.output(next_pin, not GPIO.input(next_pin))

    def color_test(self, channel, frequency, speed, step):
        p = GPIO.PWM(channel, frequency)
        p.start(0)
        try:
            while True:
                for dutyCycle in range(0, 101, step):
                    p.ChangeDutyCycle(dutyCycle)
                    time.sleep(speed)
                for dutyCycle in range(100, -1, -step):
                    p.ChangeDutyCycle(dutyCycle)
                    time.sleep(speed)
        except KeyboardInterrupt:
            print("thread exiting")

    def color_test_thread(self):
        threads = []
        threads.append(threading.Thread(target=self.color_test,
                                        args=(self.pins[0], 300, 0.02, 5)))
        threads.append(threading.Thread(target=self.color_test,
                                        args=(self.pins[1], 300, 0.035, 5)))
        threads.append(threading.Thread(target=self.color_test,
                                        args=(self.pins[2], 300, 0.045, 5)))
        for t in threads:
            t.daemon = True
            t.start()
        for t in threads:
            t.join()


if __name__ == "__main__":
    print("\nPress ^C to exit the program.\n")

    rgbled = RGBLED([3, 5, 7])
    rgbled.color_test_thread()

    

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('exiting')
    finally:
        GPIO.cleanup()
