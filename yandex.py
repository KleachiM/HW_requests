import requests

class YaUploader:
    UPL_URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, file_path: str, file_name: str, token: str):

        self.params = {'path': f'/{file_name}', 'overwrite': 'true'}
        self.headers = {'Authorization': f'OAuth {token}'}
        self.file_path = file_path
        self.file_name = file_name


    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        resp = requests.get(self.UPL_URL, params=self.params, headers=self.headers)
        put_url = resp.json().get('href')

        files = {'file': open(self.file_path + self.file_name, 'rb')}
        resp = requests.put(put_url, files=files)
        return str(resp) + ' Файл успешно загружен!'


if __name__ == '__main__':
    path = r'укажите путь'
    token = 'укажите токен'
    file_name = 'укажите файл'
    uploader = YaUploader(path, file_name, token)
    print(uploader.upload())
