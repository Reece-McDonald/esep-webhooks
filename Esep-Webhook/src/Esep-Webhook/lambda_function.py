import os
import json
import requests

def lambda_handler(event, context):
    input_data = event
    issue_url = input_data['issue']['html_url']
    payload = {'text': f'Issue Created: {issue_url}'}
    response = requests.post(os.environ.get('SLACK_URL'), json=payload)
