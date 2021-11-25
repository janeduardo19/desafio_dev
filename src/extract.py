import requests
import json


class Extract():

    def __init__(self, cont):
        self.cont = cont

    def get_api(self):
        api_url = '{0}account'.format(
            f'http://challenge.dienekes.com.br/api/numbers?page={self.cont}')

        response = requests.get(api_url)

        if response.status_code == 200:
            json_data = json.loads(response.content.decode('utf-8'))
            data_array = json_data['numbers']
            return data_array
        elif response.status_code == 500:
            # print("Status: ", response.status_code)
            return self.get_data()

    def get_data(self):
        data = []

        while True:
            array = self.get_api()
            if len(array) <= 0 or array == []:
                break
            else:
                data += array
                print(f"Getting page {self.cont}")
                self.cont += 1
                array = []

        return data
