import json
import os
import http.client

def lambda_handler(event, context):
    # Log the received event for debugging
    print(f"Received event: {event}")

    # Check if event is not an empty string
    if not event:
        return "Error: Empty input event"

    try:
        # Try to deserialize JSON
        json_data = json.loads(event)
    except json.JSONDecodeError as e:
        # Log the error for debugging
        print(f"Error decoding JSON: {str(e)}")
        return f"Error decoding JSON: {str(e)}"

    # Create payload string
    issue_url = json_data.get('issue', {}).get('html_url', '')
    payload = f"{{'text':'Issue Created: {issue_url}'}}"

    # Set up HTTP connection
    slack_url = os.environ.get("SLACK_URL")  # Get Slack URL from environment variables
    url_parts = slack_url.replace("https://", "").split("/")
    conn = http.client.HTTPSConnection(url_parts[0])

    # Set up headers
    headers = {'Content-Type': 'application/json'}

    # Send POST request
    conn.request("POST", "/" + "/".join(url_parts[1:]), body=payload, headers=headers)

    # Get response
    response = conn.getresponse()
    result = response.read().decode('utf-8')

    # Close the connection
    conn.close()

    return result
