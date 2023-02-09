import requests

class YaUploader:

    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path: str):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload_to_disk(self, file_path: str, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers = self.get_headers())
        if response.status_code == 201:
            print('Загрузка произошла успешно')


if __name__ == '__main__':
    path_to_file = '...'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload_to_disk(path_to_file, '/...')


