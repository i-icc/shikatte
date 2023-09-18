import datetime
import googleapiclient.discovery
import google.auth

class GoogleCalenderManager:
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__(self, calendar_id) -> None:
        self.calendar_id = calendar_id
        self.gapi_creds = google.auth.load_credentials_from_file('.env/gcp-key.json', self.SCOPES)[0]
        self.service = googleapiclient.discovery.build('calendar', 'v3', credentials=self.gapi_creds)

    def build_events(self, max_result = 1):
        now = datetime.datetime.utcnow().isoformat() + 'Z'

        event_list = self.service.events().list(
            calendarId=self.calendar_id, timeMin=now,
            maxResults=max_result, singleEvents=True,
            orderBy='startTime').execute()
        
        event_list_items = event_list.get('items', [])
        self.events = [(event['start'].get('dateTime', event['start'].get('date')), # start time or day
            event['end'].get('dateTime', event['end'].get('date')), # end time or day
            event['summary']) for event in event_list_items]
        
        return self
    
    def get_events(self):
        return self.events
