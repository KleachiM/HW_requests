import os
import requests

# print(os.listdir(os.path.join('C:\учеба\основы python\9', 'files'))[0])
# print(os.listdir(r'C:\учеба\основы python\9\files')[0])
# path = os.path.join('C:\учеба\нетология\основы Py\9', 'files')
path = r'C\new'


headers = {'Authorization': 'OAuth AgAAAAA86I9wAADLW4TMFaX010u7pssNYZgHB8w'}
params = {'path': path}
# print(params)
resp = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources', params = params, headers=headers)
print(resp.status_code)
print(resp.text)