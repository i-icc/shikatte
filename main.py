import config
from googleCalenderManager import GoogleCalenderManager
from serialManager import SerialManager
from soundPlayer import SoundPlayer
from time import sleep

def main():
    device_name = config.DEVICE_NAME
    # calender_id = config.CALENDER_ID
    # gcm = GoogleCalenderManager(calender_id)
    sound_manager = SoundPlayer()
    
    try:
        serial_manager = SerialManager(device_name)
    except:
        print("デバイスがみつかりませんでした。")
        
    while True:
        if serial_manager.read() < 200:
            sound_manager.buildWave().play()
            serial_manager.readAll()
            


if __name__ == "__main__":
    main()
