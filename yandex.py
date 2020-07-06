import requests
import os

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create(self):
        """Метод создает папку на Яндекс.Диске"""
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': self.file_path}
        resp = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources', params = params, headers = headers)

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        file_list = os.listdir(self.file_path)
        for file in file_list:

        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    path = r'C:\учеба\основы python\9\files'
    token = 'AgAAAAA86I9wAADLW4TMFaX010u7pssNYZgHB8w'
    uploader = YaUploader(path)
    result = uploader.upload()