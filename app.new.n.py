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
from selenium.webdriver.chrome.options import Options

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
@app.route("/", methods=['GET','POST']) #("/", methods=['GET','POST'])
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
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
#        options.add_argument("headless")
        options.add_argument("--disable-gpu")
#        options.add_argument("--no-startup-window")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0")
#        prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2, 'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}

        options.add_experimental_option("prefs", prefs)
        request_yandex_search = req["request"]["command"]
        url = settings.BASE_URL.format(request_yandex_search)
        print(url)
#        driver_bw = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
        driver_bw = webdriver.PhantomJS(executable_path='/usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs', service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']) ##'--ssl-client-certificate-file=/etc/ssl/certs/ca-certificates.crt']) ##'--ssl-client-key-file=/etc/ssl/private/ssl-cert-snakeoil.key'])##executable_path##webdriver.Chrome() ## webdriver.Chrome() ##chrome_options=option## ChromeDriverManager().install()
        
        bw_page_source = readtext.req_yand(driver_bw, url)
        print(bw_page_source)
        list_sites = readtext.parse_sites(bw_page_source)
        print(list_sites)
        get_source = readtext.go_site(driver_bw, list_sites)
##        list_parse_text = readtext.parse_text_site(get_source)
        
##        list_text_read_alisa = readtext.read_text(list_parse_text)   
#        response["response"]["text"] = "Nice"
#        if req["request"]["original_utterance"].lower() in ["природа"]:
#            response["response"]["text"] = "Nice"
#        for list in list_text_read_alisa:
#            response["response"]["text"] = list        
        driver_bw.close()
#        driver_bw.quit()
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
