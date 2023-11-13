import json
import os
import http.client

def lambda_handler(event, context):
    # Assuming `event` is a dictionary containing the input data

    # Deserialize JSON
    json_data = json.loads(json.dumps(event))

    # Access the 'issue' key directly
    issue_url = json_data.get('issue', {}).get('html_url', '')

    # Create payload string
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
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
