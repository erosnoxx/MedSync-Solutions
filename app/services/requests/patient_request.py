import urllib.parse
import urllib.request
import json


def InsertPatient(**kwargs):
    try:
        url = 'http://127.0.0.1:5000/api/v1/patient/add/'
        data = json.dumps(kwargs, default=str).encode("utf-8")
        headers = {'Content-Type': 'application/json'}
        req = urllib.request.Request(url, data=data, headers=headers)

        with urllib.request.urlopen(req) as response:
            response_data = response.read()
            response_json = json.loads(response_data.decode('utf-8'))
            return response_json
    except Exception as e:
        return {
            'message': str(e),
            'statuscode': 400
        }