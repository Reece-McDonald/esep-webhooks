import os
import json
import requests

def lambda_handler(event, context):
    try:
        # Parse the GitHub webhook event
        data = json.loads(event['body'])
        repository_name = data['repository']['full_name']
        issue_title = data['issue']['title']
        issue_url = data['issue']['html_url']

        # Customize the Slack message format
        slack_message = {
            'text': f'New issue in {repository_name}: *{issue_title}* - {issue_url}'
        }

        # Set your Slack incoming webhook URL
        slack_url = os.environ.get('SLACK_URL')

        # Send the message to Slack
        response = requests.post(slack_url, json=slack_message)

        if response.status_code == 200:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Message sent to Slack successfully'})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Failed to send message to Slack'})
            }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
