import requests
import os

class YaUploader:
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    upl_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, file_path: str, file_name: str, token: str):
        self.params = {'path': f'/{file_name}'}
        self.headers = {'Authorization': f'OAuth {token}'}
        self.file_path = file_path
        self.file_name = file_name
        # if self.find_path() == 404:
        #     self.create()

    # def find_path(self):
    #     """Метод проверяет, существует ли папка на Яндекс.Диске"""
    #     resp = requests.get (self.url, params=self.params, headers = self.headers)
    #     return resp.status_code
    #
    # def create(self):
    #     """Метод создает папку на Яндекс.Диске"""
    #     resp = requests.put(self.url, params=self.params, headers = self.headers)

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        resp = requests.get(self.upl_url, params=self.params, headers=self.headers)
        put_url = resp.json().get('href')

        files = {'file': open(self.file_path + self.file_name, 'rb')}
        resp = requests.put(self.upl_url, files=files)
        return resp.text


if __name__ == '__main__':
    path = 'C:/учеба/основы python/9/files/'
    token = 'AgAAAAA86I9wAADLW4TMFaX010u7pssNYZgHB8w'
    file_name = 'file1.txt'
    uploader = YaUploader(path, file_name, token)
    print(uploader.upload())
