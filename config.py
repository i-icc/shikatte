import json

with open('./.env/gcp-key.json') as f:
    d = json.load(f)
with open('./.env/env.json') as f:
    dd = json.load(f)

CLIENT_ID = d['client_id']
CALENDER_ID = dd['calender_id']
DEVICE_NAME = dd["device_name"]
