from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, device_id, name):
        self.__device_id = device_id
        self.__name = name
        self.__status = "OFF"

    def get_id(self):
        return self.__device_id

    def turn_on(self):
        self.__status = "ON"

    def turn_off(self):
        self.__status = "OFF"

    def get_status(self):
        return self.__status

    @abstractmethod
    def power_usage(self, hours):
        pass


class Light(Device):
    def __init__(self, device_id, name, watt):
        super().__init__(device_id, name)
        self.watt = watt

    def power_usage(self, hours):
        return (self.watt * hours) / 1000


class Fan(Device):
    def __init__(self, device_id, name, speed):
        super().__init__(device_id, name)
        self.speed = speed

    def power_usage(self, hours):
        return (self.speed * 50 * hours) / 1000


class AC(Device):
    def __init__(self, device_id, name, ton, mode):
        super().__init__(device_id, name)
        self.ton = ton
        self.mode = mode

    def power_usage(self, hours):
        if self.mode == "COOL":
            return self.ton * 1.5 * hours
        else:  # DRY
            return self.ton * 1.0 * hours


# -------- Main Program --------
n = int(input())
devices = {}

for _ in range(n):
    data = input().split()
    dtype = data[0]

    if dtype == "L":
        device_id = int(data[1])
        name = data[2]
        watt = int(data[3])
        devices[device_id] = Light(device_id, name, watt)

    elif dtype == "F":
        device_id = int(data[1])
        name = data[2]
        speed = int(data[3])
        devices[device_id] = Fan(device_id, name, speed)

    elif dtype == "A":
        device_id = int(data[1])
        name = data[2]
        ton = float(data[3])
        mode = data[4]
        devices[device_id] = AC(device_id, name, ton, mode)

q = int(input())

for _ in range(q):
    cmd = input().split()

    if cmd[0] == "ON":
        device_id = int(cmd[1])
        devices[device_id].turn_on()

    elif cmd[0] == "OFF":
        device_id = int(cmd[1])
        devices[device_id].turn_off()

    elif cmd[0] == "STATUS":
        device_id = int(cmd[1])
        print(f"Device {device_id} is {devices[device_id].get_status()}")

    elif cmd[0] == "POWER":
        device_id = int(cmd[1])
        hours = int(cmd[2])

        device = devices[device_id]
        if device.get_status() == "OFF":
            print(f"Device {device_id} is OFF")
        else:
            usage = device.power_usage(hours)
            print(f"Power used by {device_id}: {usage:.2f}")
