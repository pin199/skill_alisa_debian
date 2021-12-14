from flask import Flask, request
import logging
import json
import webbrowser as wb
from bs4 import BeautifulSoup
import settings
import requests
import readtext
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
"""
def parse_content(content):
	soup = BeautifulSoup(content, "html.parser")
	boxes = soup.find_all('li', class_="serp-item")
	href_search = []
	for box in boxes:
		link = box.find('a', class_='Link Link_theme_normal OrganicTitle-Link Typo Typo_text_l Typo_line_m organic__url link i-bem link_js_inited').attrs['href']
		logging.info(print(link))
		href_search.append(link)
	return href_search
"""
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

tif req["session"]["new"]:
ttresponse["response"]["text"] = "Браузер открыт. Жду Ваш запрос?"
telse:
ttrequest_yandex_search = req["request"]["command"]
tturl = settings.BASE_URL.format(request_yandex_search)
ttdriver_bw = webdriver.Chrome(ChromeDriverManager().install())
ttbw_page_source = readtext.req_yand(driver_bw, url)
ttlist_sites = readtext.parse_sites(bw_page_source)
ttget_source = readtext.go_site(driver_bw, list_sites)
ttlist_parse_text = parse_text_site(get_source)
ttreadtext.read_text(list_parse_text)
ttdriver_bw.close()
tt
#		wb.open_new_tab(url)
#		response_url = requests.get(url)
#		list_search = parse_content(response_url.text)
#		wb.open_new_tab(list_search[0])
ttresponse["response"]["text"]= "Nice" 
#		if req["request"]["command"] == "хорошо":
#			response["response"]["text"] = "Отлично"
#		elif:
#			response["response"]["text"] = "Ошибка"

	return json.dumps(response)	
