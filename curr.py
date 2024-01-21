import requests
import csv

def fetch_rates():
    # get json and convert to python list of dicts
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    
    # convert list into a dict and extract 'rates' value (a list)
    dct = {}
    for i in data:
        dct.update(i)
    return dct['rates']

def list_to_csv(data_list, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_list[0].keys(), delimiter=';')
        
        writer.writeheader()
        # [:-1] to trim last line
        writer.writerows(data_list[:-1])


rates_list = fetch_rates()
csv_file = 'output.csv'
list_to_csv(rates_list, csv_file)