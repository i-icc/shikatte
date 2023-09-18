import json

with open('./.env/gcp-key.json') as f:
    d = json.load(f)

CLIENT_ID = d['client_id']
