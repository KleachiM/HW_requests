import requests
import os

headers = {'Authorization': 'OAuth AgAAAAA86I9wAADLW4TMFaX010u7pssNYZgHB8w'}

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        resp = requests.put ( 'https://cloud-api.yandex.net:443/v1/disk/resources?path=%5CC%5Cnew%5C',
                              headers = headers )
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    path = os.path.join ( 'C:\учеба\нетология\основы Py\9', 'files' )
    uploader = YaUploader(path)
    result = uploader.upload()