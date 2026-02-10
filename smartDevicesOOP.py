#OOP Practice inheritance & encapsulation
class smartDevices:
    def __init__(self,device_name,is_on,serial_number):
        self.device_name=device_name #Public
        self._is_on = False #Protected
        self.__serial_number=serial_number #Private
    def toggle_power(self):
        if _is_on == True:
            return False
        elif _is_on == False:
            return True
#Subclass-->Inheritance
class thermostat(smartDevices):
    def __init__(self,temperature):
        super().__init__(device_name,__serial_number)
    def set_temp(self,new_temp):
        if _is_on == True:
            self.temperature = new_temp
class securityCamera(smartDevices):
    def __init__(self,is_recording):
        self._is_recording = _is_recording
        super().init(device_name,__serial_number)
        super().toggle_power()
        if _is_on == False:
            self._is_recording = False
            