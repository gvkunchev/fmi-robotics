import smbus
import math
import time

class Pwm:
    "PCA9685 16-Channel 12-Bit I2C BUS PWM Driver in Pi B+"
    
    _frequency      = 60

    _MODE1          = 0x00
    _MODE2          = 0x01
    _SUBADR1        = 0x02
    _SUBADR2        = 0x03
    _SUBADR3        = 0x04
    _PRESCALE       = 0xFE
    _LED0_ON_L      = 0x06
    _LED0_ON_H      = 0x07
    _LED0_OFF_L     = 0x08
    _LED0_OFF_H     = 0x09
    _ALL_LED_ON_L   = 0xFA
    _ALL_LED_ON_H   = 0xFB
    _ALL_LED_OFF_L  = 0xFC
    _ALL_LED_OFF_H  = 0xFD
    _RESTART        = 0x80
    _SLEEP          = 0x10
    _ALLCALL        = 0x01
    _INVRT          = 0x10
    _OUTDRV         = 0x04
    
    def __init__(self, bus_number=1, address=0x40):
        self.bus_number = bus_number
        self.address = address
        self._assign_bus()
        self.set_all_value(0, 0)
        self._init_mode1()
        self._init_mode2()
        time.sleep(0.005)
        self._disable_sleep_mode()
        time.sleep(0.005)
        self._set_frequency(self._frequency)
    
    def _init_mode1(self):
        self._write_byte_data(self._MODE1, self._ALLCALL)
    
    def _init_mode2(self):
        self._write_byte_data(self._MODE2, self._OUTDRV)

    def _assign_bus(self):
        self.bus = smbus.SMBus(self.bus_number)
    
    def _write_byte_data(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)

    def _read_byte_data(self, reg):
        results = self.bus.read_byte_data(self.address, reg)
        return results
    
    def _enable_restart(self):
        old_mode = self._read_byte_data(self._MODE1)
        new_mode = old_mode | self._RESTART
        self._write_byte_data(self._MODE1, new_mode)
      
    def _disable_restart(self):
        old_mode = self._read_byte_data(self._MODE1)
        new_mode = old_mode & ~self._RESTART
        self._write_byte_data(self._MODE1, new_mode)
    
    def _disable_sleep_mode(self):
        old_mode = self._read_byte_data(self._MODE1)
        new_mode = old_mode | self._SLEEP
        self._write_byte_data(self._MODE1, new_mode)
    
    def _disable_sleep_mode(self):
        old_mode = self._read_byte_data(self._MODE1)
        new_mode = old_mode & ~self._SLEEP
        self._write_byte_data(self._MODE1, new_mode)
    
    def _get_mode1(self):
        return self._read_byte_data(self._MODE1)
    
    def _set_mode1(self, mode):
        return self._write_byte_data(self._MODE1, mode)
    
    def _calculate_frequency(self, freq):
        prescale_value = 25000000.0
        prescale_value /= 4096.0
        prescale_value /= float(freq)
        prescale_value -= 1.0
        return int(math.floor(round(prescale_value)))

    def _set_frequency(self, freq):
        old_mode = self._get_mode1()
        self._disable_restart()
        self._disable_sleep_mode()
        self._write_byte_data(self._PRESCALE, self._calculate_frequency(freq))
        self._set_mode1(old_mode)
        time.sleep(0.005)
        self._enable_restart()

    def set_value(self, channel, on, off):
        self._write_byte_data(self._LED0_ON_L + 4*channel, on & 0xFF)
        self._write_byte_data(self._LED0_ON_H + 4*channel, on >> 8)
        self._write_byte_data(self._LED0_OFF_L + 4*channel, off & 0xFF)
        self._write_byte_data(self._LED0_OFF_H + 4*channel, off >> 8)

    def set_all_value(self, on, off):
        self._write_byte_data(self._ALL_LED_ON_L, on & 0xFF)
        self._write_byte_data(self._ALL_LED_ON_H, on >> 8)
        self._write_byte_data(self._ALL_LED_OFF_L, off & 0xFF)
        self._write_byte_data(self._ALL_LED_OFF_H, off >> 8)
