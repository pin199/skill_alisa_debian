from flask import Flask, request
from selenium import webdriver
import logging
import json
import webbrowser as wb
from bs4 import BeautifulSoup
import settings
import requests
import readtext
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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
@app.route("/", methods=['POST']) #("/", methods=['GET','POST'])
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
#        response["response"]["text"] = "Good"
        start_time = time.time()
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
#        prefs = {"profile.manager_default_content_settings.images":2,"permissions.default.stylesheet":2}
#        options.add_experimental_option("prefs", prefs)
        request_yandex_search = req["request"]["command"]
        url = settings.BASE_URL.format(request_yandex_search)
        server_url = "http://127.0.0.1:8000"
        dc = DesiredCapabilities.HTMLUNIT
        driver_bw = webdriver.Remote(server_url, dc)
#        driver_bw = webdriver.HtmlUnitDriver()##Chrome(options=options)##webdriver.Chrome() ## webdriver.Chrome() ##chrome_options=option## ChromeDriverManager().install()
        bw_page_source = readtext.req_yand(driver_bw, url)
        list_sites = readtext.parse_sites(bw_page_source)
        get_source = readtext.go_site(driver_bw, list_sites)
        list_parse_text = readtext.parse_text_site(get_source)
        
        list_text_read_alisa = readtext.read_text(list_parse_text)   
#        response["response"]["text"] = "Nice"
#        if req["request"]["original_utterance"].lower() in ["природа"]:
#            response["response"]["text"] = "Nice"
#        for list in list_text_read_alisa:
#            response["response"]["text"] = list        
        driver_bw.close()
        driver_bw.quit()
        print("--- %s seconds ---" % (time.time() - start_time))
        response["response"]["text"] = "Nice" 
#		wb.open_new_tab(url)
#		response_url = requests.get(url)
#		list_search = parse_content(response_url.text)
#		wb.open_new_tab(list_search[0])
#        response["response"]["text"]= "Nice" 
#		if req["request"]["command"] == "хорошо":
#			response["response"]["text"] = "Отлично"
#		elif:
#			response["response"]["text"] = "Ошибка"
    return json.dumps(response)	
