import requests
from bs4 import BeautifulSoup

page = requests.get("https://uzxit.net/arab-mp3")
soup = BeautifulSoup(page.content, "html.parser")

arab_f: list[str] = []
# job_elements = soup.find_all("div", class_="cols fx-row")
data = soup.find_all("div", class_="track-item fx-row fx-middle js-item js-share-item")
for x in data:
    data_track_value = x.get("data-track")
    arab_f.append(data_track_value)
    print(data_track_value)
