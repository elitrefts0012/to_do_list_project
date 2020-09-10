from pprint import pprint
import requests


email = 'admin@admin.com'
password = 'test'
post_dict = {
    'for_sale': True,
    'stock_quantity': 3,
    'price': 200,
    'manufacturer': 'Armalite',
    'model': 'AR-17',
    'caliber': '12 Gauge',
    'current_owner': 'Totally Legal Gun Salesman',
}


class ApiTester:
    def __init__(self, email, password):
        self.base_url = 'http://localhost/api/'
        self.guns_url = f'{self.base_url}guns/'

        auth_key = self.authenticate(email, password)
        self.auth_header = {
            'Authorization': f'Token {auth_key}',
        }

    def authenticate(self, email, password):
        auth_url = f'{self.base_url}auth/login/'
        creds = {
            'email': email,
            'password': password,
        }
        resp = requests.post(auth_url, creds)
        key_dict = resp.json()
        return key_dict['key']

    def gun_list(self):
        resp = requests.get(f'{self.guns_url}?', headers=self.auth_header)
        print('resp.status_code', resp.status_code)
        print('resp.json')
        pprint(resp.json())

    def create_gun(self, gun_data):
        resp = requests.post(self.guns_url, gun_data, headers=self.auth_header)
        pprint(resp.status_code)
        pprint(resp.json())


t = ApiTester(email, password)
t.create_gun(post_dict)
# t.gun_list()
