class Device:
    def turn_on(self):
        print("Device is now ON")

    def turn_off(self):
        print("Device is now OFF")

    def set_temperature(self, temperature):
        print(f"Temperature set to {temperature}°")


class Light(Device):
    def set_temperature(self, temperature):
        raise Exception("Lights do not support temperature control.")


class Thermostat(Device):
    def set_temperature(self, temperature):
        print(f"Thermostat temperature set to {temperature}°")


def main():
    devices = {
        "1": Light(),
        "2": Thermostat()
    }

    while True:
        print("1. Light")
        print("2. Thermostat")
        print("3. Exit")

        choice = input("Select device: ")

        if choice == "3":
            break
        if choice not in devices:
            print("Invalid device.\n")
            continue

        device = devices[choice]

        print("1. Turn On")
        print("2. Turn Off")
        print("3. Set Temperature")

        action = input("Choose action: ")

        try:
            if action == "1":
                device.turn_on()
            elif action == "2":
                device.turn_off()
            elif action == "3":
                temp = int(input("Enter temperature: "))
                device.set_temperature(temp)
            else:
                print("Invalid action.")
        except Exception as e:
            print("Error:", e)

        print()


if __name__ == "__main__":
    main()