import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# サービスアカウントキーのパスを指定して認証情報を読み込みます
credentials = service_account.Credentials.from_service_account_file(
    '.env/gcp-key.json',
    scopes=['https://www.googleapis.com/auth/calendar.readonly']
)

# カレンダーAPIクライアントを作成します
service = build('calendar', 'v3', credentials=credentials)

# 今日の日付を取得します
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z'はUTC時間を指定

# イベントを取得します
events_result = service.events().list(
    calendarId='primary',  # カレンダーIDを指定
    timeMin=now,
    maxResults=10,  # 取得するイベントの最大数
    singleEvents=True,
    orderBy='startTime'
).execute()

events = events_result.get('items', [])

if not events:
    print('予定はありません')
else:
    print('次の予定:')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f'{start} - {event["summary"]}')
