import config
from googleCalenderManager import GoogleCalenderManager

def main():
    calender_id = config.CALENDER_ID
    gcm = GoogleCalenderManager(calender_id)
    gcm.build_events()
    print(gcm.get_events())

if __name__ == "__main__":
    main()
