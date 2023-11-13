import json
import os
import http.client

def lambda_handler(event, context):
    jdata = json.loads(json.dumps(event))
        
    payload = f"{{'text':'Issue Created: {json.issue.html_url}'}}";
    
    
    headers = {'Content-Type': 'application/json'}
    slack_url = os.environ.get("SLACK_URL")
    url_parts = slack_url.replace("https://", "").split("/")
    conn = http.client.HTTPSConnection(url_parts[0])
    
    conn.request("POST", "/" + "/".join(url_parts[1:]), body=payload, headers=headers)
    response = conn.getresponse()
    result = response.read().decode('utf-8')
    
    conn.close()
        
    return result;
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
