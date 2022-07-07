import requests

def backend_call(payload):
    backend_url='https://autocertapi.azurewebsites.net/create'
    r = requests.post(backend_url, json=payload)
    return r.status_code
