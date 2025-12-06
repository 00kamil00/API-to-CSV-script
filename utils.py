import requests
import csv


def fetch_data(url):
    response = requests.get(url)    
    response.raise_for_status()
    return response.json()

def process_data(raw_data):
    wyniki = [] 
    for item in raw_data:
        wyniki.append({
            'name': item['name'],
            'username': item['username'],
            'city': item['address']['city'],
            'phone': item['phone'],
            'email': item['email']
        })
    return wyniki 

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'username', 'city', 'phone', 'email'])
        writer.writeheader()
        writer.writerows(data)
