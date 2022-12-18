from .hardware.motor import Motor


class Transmission:
    "Transmission of the car. It controls the two motors' direction."

    def __init__(self, left_fwd, left_bwd, right_fwd, right_bwd):
        """Initializator."""
        self._motor_left = Motor(fwd=left_fwd, bwd=left_bwd)
        self._motor_right = Motor(fwd=right_fwd, bwd=right_bwd)

    def fwd(self):
        """Move forward."""
        self._motor_left.fwd()
        self._motor_right.fwd()

    def bwd(self):
        """Move backward."""
        self._motor_left.bwd()
        self._motor_right.bwd()

    def stop(self):
        """Stop moving."""
        self._motor_left.stop()
        self._motor_right.stop()
