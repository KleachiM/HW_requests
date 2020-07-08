import requests
import os

class YaUploader:
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    upl_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, file_path: str, token: str):
        self.params = {'path': file_path}
        self.headers = {'Authorization': f'OAuth {token}'}
        if self.find_path() == 404:
            self.create()

    def find_path(self):
        """Метод проверяет, существует ли папка на Яндекс.Диске"""
        resp = requests.get (self.url, params=self.params, headers = self.headers)
        return resp.status_code

    def create(self):
        """Метод создает папку на Яндекс.Диске"""
        resp = requests.put(self.url, params=self.params, headers = self.headers)

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        resp = requests.get(self.upl_url, params = self.params, headers = self.headers)
        put_url = resp.json().get( 'href' )
        # print(put_url)


if __name__ == '__main__':
    path = r'C\new'
    token = 'AgAAAAA86I9wAADLW4TMFaX010u7pssNYZgHB8w'
    uploader = YaUploader(path, token)
    uploader.upload()