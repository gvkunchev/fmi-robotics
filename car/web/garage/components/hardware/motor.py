import RPi.GPIO as GPIO


class Motor:
    "Basic motor, that can turn forwards and backwards."

    def __init__(self, fwd, bwd):
        """Initializator."""
        self._fwd = fwd
        self._bwd = bwd
        self._set_board()

    def _set_board(self):
        """Reserve and initiate the GPIO pins."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._fwd, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self._bwd, GPIO.OUT, initial=GPIO.LOW)

    def fwd(self):
        """Move forward."""
        GPIO.output(self._fwd, GPIO.HIGH)
        GPIO.output(self._bwd, GPIO.LOW)

    def bwd(self):
        """Move backward."""
        GPIO.output(self._fwd, GPIO.LOW)
        GPIO.output(self._bwd, GPIO.HIGH)

    def stop(self):
        """Stop moving."""
        GPIO.output(self._fwd, GPIO.LOW)
        GPIO.output(self._bwd, GPIO.LOW)

    def __del__(self):
        """Release all GPIO pins."""
        GPIO.cleanup()
