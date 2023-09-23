import config
from googleCalenderManager import GoogleCalenderManager

def main():
    gcm = GoogleCalenderManager()
    gcm.build_events()
    print(gcm.get_events())

if __name__ == "__main__":
    main()
