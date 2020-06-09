import requests

key = "AIzaSyBDDBiCGNkpnRAw7GUJDOOhnYg0HDIDrC8"
url = "https://www.googleapis.com/youtube/v3/search"






search = input("검색어를 입력하세요 : ")
q = f"q={search}"
my_type = "type=video"
part = "part=snippet"
maxResults = "maxResults=20"
requestUrl = f"{url}?key={key}&{part}&{my_type}&{q}&{maxResults}"

response = requests.get(requestUrl)
data = response.json()

for i in data['items']:
    print(i['snippet']['title'],i['snippet']['channelTitle'])



"https://www.youtube.com/watch?v=lujgRCb462g"