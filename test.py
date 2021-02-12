import requests

payload = {
    'source_account': 'Source',
    'target_account': 'Target',
    'amount': 50
}

result = requests.post('http://localhost:5000/transfer', json=payload)
print(result.status_code)