import serial


class SerialManager:

    def __init__(self, device: str = '/dev/ttyACM0', port: int = 9600, timeout: int = 1) -> None:
        self.ser = serial.Serial(device, port, timeout=timeout)
        self.ser.flush()

    def read(self) -> int:
        line: str = "1023"
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
        try:
            return int(line)
        except:
            return -1
        
    def readAll(self):
        self.ser.read_all()


if __name__ == "__main__":
    device_name = "/dev/tty.usbserial-130"
    try:
        serial_manager = SerialManager(device_name)
        while True:
            print(serial_manager.read())
    except Exception as err:
        print(err)
