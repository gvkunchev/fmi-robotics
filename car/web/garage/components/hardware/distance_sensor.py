import RPi.GPIO as GPIO
import time


class DistanceSensor:
    """HC-SR04 Ultrasonic distance sensor."""

    def __init__(self, trig, echo):
        """Initializator."""
        self._trig = trig
        self._echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self._echo, GPIO.IN)
    
    def read(self):
        """Calculate distance in cm and return it."""
        GPIO.output(self._trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self._trig, GPIO.LOW)
        while not GPIO.input(self._echo):
            pulse_start = time.time()
        while GPIO.input(self._echo):
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17165 # Half the speed of sound in cm/s
        return round(distance, 1)

    def __del__(self):
        """Release the pins."""
        GPIO.cleanup()
