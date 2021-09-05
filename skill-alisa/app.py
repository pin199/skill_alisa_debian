from flask import Flask, request
import logging
import json
import webbrowser as wb
from bs4 import BeautifulSoup
import settings
import requests

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def parse_content(content):
	soup = BeautifulSoup(content, "html.parser")
	boxes = soup.find_all('li', class_="serp-item")
	href_search = []
	for box in boxes:
		link = box.find('a', class_='Link Link_theme_normal OrganicTitle-Link Typo Typo_text_l Typo_line_m organic__url link i-bem link_js_inited').attrs['href']
		logging.info(print(link))
		href_search.append(link)
	return href_search

@app.route("/", methods=['GET','POST'])
def main():
	logging.info(request.json)
	response = {
		"version": request.json["version"],
		"session": request.json["session"],
		"response":{
			"end_session": False
		}
	}
	
	req = request.json

	if req["session"]["new"]:
		response["response"]["text"] = "Браузер открыт. Жду Ваш запрос?"
	else:
		request_yandex_search = req["request"]["command"]
		url = settings.BASE_URL.format(request_yandex_search)
		wb.open_new_tab(url)
		response_url = requests.get(url)
		list_search = parse_content(response_url.text)
		wb.open_new_tab(list_search[0])
		response["response"]["text"]= "Nice" 
#		if req["request"]["command"] == "хорошо":
#			response["response"]["text"] = "Отлично"
		#elif:
		#	response["response"]["text"] = "Ошибка"

	return json.dumps(response)	
