import requests
import json
def joke():
  response=requests.get("https://api.vvhan.com/api/xh?type=json")
  json_data = json.loads(response.text)
  return json_data["joke"]