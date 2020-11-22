import requests

def consulta():
    response = requests.get('http://localhost:5000/pessoa')
    print(response.status_code)
    print(response.json())
    