import pandas as pd
import glob
import numpy as np
import json
import requests
url = 'http://ec2-100-26-152-194.compute-1.amazonaws.com:3000/battles/1'
datos = {'Token': '11360e9d-0fdc-49d4-b127-aec80336c6a9', 'content-type': 'application/json'}
resp = requests.get(url, headers=datos)
print(type(resp.content))
print(type(resp.text))
print(type(resp.json()))
df = pd.read_json(resp.text)
