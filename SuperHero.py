import requests
from pprint import pprint

class Super_Hero:

    base_host = 'https://akabab.github.io/superhero-api/api'

    def get_all_id(self):
        uri = '/all.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        res = response.json()
        # pprint(res)
        for heroes in res:
            if heroes['name'] == 'Hulk':
                print(f'ID Hulk: {heroes["id"]}')
            elif heroes['name'] == 'Captain America':
                print((f'ID Captain America: {heroes["id"]}'))
            elif heroes['name'] == 'Thanos':
                print((f'ID Thanos: {heroes["id"]}'))


    def get_intelligence_ca(self):
        uri = '/powerstats/149.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        res = response.json()
        global ca
        ca = res['intelligence']

    def get_intelligence_hulk(self):
        uri = '/powerstats/332.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        res = response.json()
        global hulk
        hulk = res['intelligence']

    def get_intelligence_thanos(self):
        uri = '/powerstats/655.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        res = response.json()
        global thanos
        thanos = res['intelligence']

        if ca < hulk > thanos:
            print(f'Самый умный супергерой Hulk')
        elif hulk < ca > thanos:
            print(f'Самый умный супергерой Captain America')
        else:
            print(f'Самый умный супергерой Thanos')


if __name__ == '__main__':
    sh = Super_Hero()
    sh.get_all_id()
    sh.get_intelligence_ca()
    sh.get_intelligence_hulk()
    sh.get_intelligence_thanos()




