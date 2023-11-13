import json
import os
import urllib.request
from http.client import HTTPResponse

def lambda_handler(event, context):
    try:
        json_data = json.loads(event)
    except json.JSONDecodeError as e:
        return {
            "errorMessage": f"Error decoding JSON: {str(e)}",
            "errorType": "JSONDecodeError"
        }

    payload = f"{{'text':'Issue Created: {json_data['issue']['html_url']}'}}"

    url = os.environ.get("SLACK_URL")
    request_data = payload.encode("utf-8")
    headers = {"Content-Type": "application/json"}

    request = urllib.request.Request(url, data=request_data, headers=headers, method="POST")
    with urllib.request.urlopen(request) as response:  # type: HTTPResponse
        return response.read().decode("utf-8")
