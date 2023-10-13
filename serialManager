import serial


class SerialManager:

    def __init__(self, device: str = '/dev/ttyACM0', port: int = 9600, timeout: int = 1) -> None:
        self.ser = serial.Serial(device, port, timeout=timeout)
        self.ser.flush()

    def read(self) -> str:
        line: str = ""
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
        return line
