import json
import os
import requests

def lambda_handler(event, context):
    # issue_url grabs the url of the issue that has been interacted with. Grabs it from 'event', which is of type dictionary.
    issue_url = event['issue']['html_url']
    # payload generates the json 'text' to be printed in slack, being 'Issue Created: issue_url'.
    payload = {'text': f'Issue Created: {issue_url}'}
    # response uses the requests library to send the text to the slack channel, using the environment variable
    # that contains the URL to post to the channel, and sets the json data to the payload data.
    response = requests.post(os.environ.get('SLACK_URL'), json=payload)
