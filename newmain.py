from abc import ABC, abstractmethod

# Base contract every device must fulfill
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Optional capability - only devices taht truly support it implement this
class TemperatureControllable(ABC):
    @abstractmethod
    def set_temperature(self, temperature):
        pass


# Light fulfills the full device contract - no unsupported methods
class Light(Device):
    def turn_on(self):
        print("Light is now ON")

    def turn_off(self):
        print("Light is now OFF")

    
# Thermostat fulfills Device + the optional temperature interface
class Thermostat(Device, TemperatureControllable):
    def turn_on(self):
        print("Thermostat is now ON")

    def turn_off(self):
        print("Thermostat is now OFF")

    def set_temperature(self, temperature):
        print(f"Thermostat temperature is set to {temperature}°")


def handle_device(device: Device):
    print("1. Turn On")
    print("2. Turn Off")

    # Menu option only appears if the device actually supports it
    if isinstance(device, TemperatureControllable):
        print("3. Set Temperature")

    action = input("Choose action: ")

    if action == "1":
        device.turn_on()
    elif action == "2":
        device.turn_off()
    elif action == "3" and isinstance(device, TemperatureControllable):
        temp = int(input("Enter temperature: "))
        device.set_temperature(temp)
    else:
        print("Invalid action.")


def main():
    devices = {
        "1": Light(),
        "2": Thermostat(),
    }
    
    while True:
        print("\n1. Light")
        print("2. Thermostat")
        print("3. Exit")

        choice = input("Select device: ")

        if choice == "3":
            break
        if choice not in devices:
            print("Invalid device.")
            continue
    
        handle_device(devices[choice])

if __name__ == "__main__":
    main()