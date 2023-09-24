import datetime
import google
from googleapiclient.discovery import build

class GoogleCalenderManager:
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def __init__(self, calendar_id:str = 'primary') -> None:
        self.calendar_id = calendar_id
        self.gapi_creds = google.auth.load_credentials_from_file('.env/gcp-key.json', self.SCOPES)[0]
        self.service = build('calendar', 'v3', credentials=self.gapi_creds)

    def build_events(self, max_result:int = 1):
        now = datetime.datetime.utcnow().isoformat() + 'Z'

        self.events = self.service.events().list(
                calendarId=self.calendar_id, 
                timeMin=now,
                maxResults=max_result,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
        
        return self
    
    def get_formated_events(self):
        event_list_items = self.events.get('items', [])
        return [(event['start'].get('dateTime', event['start'].get('date')), # start time or day
            event['end'].get('dateTime', event['end'].get('date')), # end time or day
            event['summary']) for event in event_list_items]
        
    
    def get_events(self):
        return self.events
