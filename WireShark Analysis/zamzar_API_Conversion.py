'''
Created on Sep 23, 2016

@author: Sushant
'''

import requests
from requests.auth import HTTPBasicAuth

api_key = '2709f66c5a5fa1adb10ee6938de37aa5c4eb9182'
endpoint = "https://sandbox.zamzar.com/v1/jobs"
source_file = "/tmp/portrait.gif"

# '/Users/sushantpatil/Desktop/Project HawkEye/In Progress/Bread Furst/Workbook copy 2.xlsx'
target_format = "xlsx"

file_content = {'source_file': open(source_file, 'rb')}
data_content = {'target_format': target_format}
res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
print res.json()