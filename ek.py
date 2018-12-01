#/usr/bin/python3

# This is a basic wrapper for getting the image descriptions

import requests
import json
import base64
import glob
import time

def get_keys():
	cred = {}
	with open("keys") as f:
		lines = f.readlines()
	for line in lines:
		key,value = line.split("\t")
		cred[key] = value.replace("\n","")

	return cred

def get_description(image):
 
    with open(image, 'rb' ) as f:
        data = f.read()
   
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key' : cred['azure_key']
    }
   
    r = requests.request( 'post', 'https://eastus.api.cognitive.microsoft.com/vision/v1.0/describe', json = '', data = data, headers = headers)

    d = json.loads(str(r.content,'utf-8'))

    if 'description' in d:
        if (len(d['description']['captions']) > 0):
            return d['description']['captions'][0]['text'].replace("a close up of ","")
        else:
            return "....."
    else:
        return "....."



cred = get_keys()

files = glob.glob("/Volumes/Untitled 2/bf/v/santa/frames/*.jpg")

for i in range(len(files)):
    text = get_description(files[i])
    print(text)
    f = open("data.tsv","a")
    f.write(files[i]+"\t"+text + "\n")


