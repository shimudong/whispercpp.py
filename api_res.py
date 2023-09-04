import json
import requests

path_wav = "./sample.wav"

url = "http://127.0.0.1:11111"
files = {'file':('wav_file', open(path_wav, 'rb'))}
r = requests.post(url, files = files)

print(json.loads(r.text))