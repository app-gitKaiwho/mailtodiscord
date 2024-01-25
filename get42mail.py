from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup
import os
import pickle
import base64
import json

param = json.load(open('token/param.json', 'r'))
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

async def get_mails():
    emails = []
    decoded_mails = []
    creds = None
    if os.path.exists('token/token.pickle'):
        with open('token/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        with open('token/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    user_info = service.users().getProfile(userId='me').execute()
    print(f"Retrieving mail from: {user_info['emailAddress']}")
    results = service.users().messages().list(userId='me',labelIds = ['UNREAD']).execute()
    messages = results.get('messages', [])
    if messages:
        for message in messages:
            msg_id = message['id']
            msg = service.users().messages().get(userId='me', id=msg_id).execute()
            if param.get('setasread'):
                service.users().messages().modify(userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()
            payload = msg['payload']
            body = payload.get('body', {})
            headers = msg['payload']['headers']
            date = sender = subject = ""
            for header in headers:
                name = header.get('name')
                if name.lower() == 'date':
                    date = header.get('value')
                elif name.lower() == 'subject':
                    subject = header.get('value')
            if 'data' in body:
                data = body['data']
                decoded_data = base64.urlsafe_b64decode(data).decode()
                decoded_data = decoded_data.split('<p>')[1].split('</p>')[0]
                decoded_data = BeautifulSoup(decoded_data, 'html.parser').text
                if (data == "" or not(decoded_data.lower().startswith('hi'))):
                    continue
            else :
                continue
            filename = f'{subject} {date}'
            filename.split('+')[0]
            emails.append(filename)
            decoded_mails.append(decoded_data.split('Hi,')[1])
    return emails, decoded_mails