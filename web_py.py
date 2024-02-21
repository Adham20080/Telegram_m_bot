import requests
from bs4 import BeautifulSoup

pag = requests.get("https://uzxit.net/uzbek-mp3")
sou = BeautifulSoup(pag.content, "html.parser")

audio: list[str] = []
# job_elements = sou.find_all("div", class_="cols fx-row")
data = sou.find_all("div", class_="track-item fx-row fx-middle js-item js-share-item")
for x in data:
    data_track_value = x.get("data-track")
    audio.append(data_track_value)
    print(data_track_value)

pag1 = requests.get("https://uzxit.net/xorazim-mp3")
sou1 = BeautifulSoup(pag1.content, "html.parser")

audio1: list[str] = []
# job_elements = sou.find_all("div", class_="cols fx-row")
data = sou1.find_all("div", class_="track-item fx-row fx-middle js-item js-share-item")
for x in data:
    data_track_value = x.get("data-track")
    audio1.append(data_track_value)
    print(data_track_value)
