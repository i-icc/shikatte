import config
from googleCalenderManager import GoogleCalenderManager

def main():
    client_id = config.CLIENT_ID
    gcm = GoogleCalenderManager(client_id)
    gcm.build_events()
    print(gcm.get_events())

if __name__ == "__main__":
    main()
