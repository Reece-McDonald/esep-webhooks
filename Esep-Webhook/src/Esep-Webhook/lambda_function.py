import os
import json
import requests

def lambda_handler(event, context):
    issue_url = event['issue']['html_url']
    payload = {'text': f'Issue Created: {issue_url}'}
    response = requests.post(os.environ.get('SLACK_URL'), json=payload)
