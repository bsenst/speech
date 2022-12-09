import requests
import time
import json

endpoint = "https://api.assemblyai.com/v2/transcript"

video_url = input("Enter video url: ")

json = {
    "video_url": video_url,
    "summarization": True,
    "summary_model": "informative",
    "summary_type": "bullets",
    "auto_chapters": True,
    "entity_detection": True,
    "iab_categories": True
}

api_token = input("Enter your API Token for Assembly.AI: ")

headers = {
    "authorization": api_token,
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

# https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
timestr = time.strftime("%Y%m%d")

# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
with open("response"+timestr+".json", "w") as outfile:
    outfile.write()
    json.dump(response.json(), outfile)