import requests
import sys
import time

URL = 'http://127.0.0.10:8080'
URI = '/record?id_nodo=nodoPrueba1&temperatura=24.5&humedad=68.2&co2=293&volatiles=112'

NUM_REQUESTS = 150000

def main():
    for i in range(NUM_REQUESTS):
        response = requests.get(f'{URL}{URI}')
        if (response.status_code == 200): 
            print(f'[{i:06}] Successful get request!')
        else: 
            print(f'[{i:06}] Failed get request!' ,file=sys.stderr)
        time.sleep(0.01)

if __name__ == '__main__':
    main()