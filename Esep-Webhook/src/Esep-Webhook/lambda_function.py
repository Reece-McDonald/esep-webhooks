import os
import json
import requests

def lambda_handler(event, context):
    try:
        # Check if event is a string or a dictionary
        if isinstance(event, str):
            input_data = json.loads(event)
        elif isinstance(event, dict):
            input_data = event
        else:
            raise ValueError("Unsupported input format")

        # Extract relevant information from the data
        issue_url = input_data['issue']['html_url']

        # Customize the Slack message format
        payload = {'text': f'Issue Created: {issue_url}'}

        # Set your Slack incoming webhook URL
        slack_url = os.environ.get('SLACK_URL')

        # Send the message to Slack using the requests library
        response = requests.post(slack_url, json=payload)

        if response.status_code == 200:
            return {'statusCode': 200, 'body': json.dumps({'message': 'Message sent to Slack successfully'})}
        else:
            return {'statusCode': 500, 'body': json.dumps({'error': 'Failed to send message to Slack'})}

    except Exception as e:
        return {'statusCode': 400, 'body': json.dumps({'error': str(e)})}
