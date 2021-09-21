from bs4 import BeautifulSoup
import requests
import webbrowser as wb
from urllib.parse import urljoin
#from python_rucaptcha import ImageCaptcha
import sys
sys.path.insert(0, "/Users/nikolaj/PythonProg/gitSkillAlisa/skill_alisa_debian/Parse/ImageRecognition")
import recim
import json
import requests
import httplib2

def parse_content(content):
	soup = BeautifulSoup(content, 'html.parser')
#	print(soup)
	boxes = soup.find_all("a") #('li', class_='serp-item')
#	print(boxes)
#	print(len(boxes))
	href_search = []
	print("1")
	for box in boxes:
		link = box.find('a', class_='Link Link_theme_normal OrganicTitle-Link Typo Typo_text_l Typo_line_m organic__url link i-bem link_js_inited').attrs['href']
		print(link)
		href_search.append(link)
	return href_search

def capcha(content_capcha):
	current_url = "https://yandex.ru/"
	soup = BeautifulSoup(content_capcha, 'html.parser')
	url_capcha = soup.find('form', class_='CheckboxCaptcha-Form').attrs['action']
#	print(url_capcha)
	link_for_post = urljoin(current_url, url_capcha)
	resp_post = requests.post(link_for_post)
	soup_resp_capcha = BeautifulSoup(resp_post.text, 'html.parser')
	url_resp_capcha = soup_resp_capcha.find('img', class_='AdvancedCaptcha-Image').attrs['src']
	print(url_resp_capcha)

	#Get image
	img = requests.get(url_resp_capcha)
	out = open("img.jpg","wb")
	out.write(img.content)
	out.close()
	
	print("test:"+recim.img_string())
	
#	solution_capcha(url_resp_capcha)
#	print(resp_post.text)

def req_search_yandex_without_capcha():
	data = {
		'Host': 'yandex.ru',
		'Cookie': 'mda=0; yandex_gid=56; yandexuid=7087684401630933978; yuidss=7087684401630933978; is_gdpr=0; is_gdpr_b=CLPnPBCARCgC; i=bmquR2QYmkC+Iu1VkNhhZArHMW0WRVAzBehX2XxY2DtfnQZCu2iFjQ6saUsGaipPr3bxDRytJg3kTgtv3tcWTeL0IDs=; font_loaded=YSv1; ymex=1946294093.yrts.1630934093; yabs-frequency=/5/0000000000000000/Wc51ROO0002eGYC0/; _ym_uid=1630934123448513266; yp=1633525979.ygu.1#1646702097.szm.1:1440x900:1387x707; my=YwA=; _yasc=un1dOzEMYzsYnesXnRFJlmxkTrP3uTGk2l3AadUOJO71+r1xunEame+H; _ym_d=1630938878',
		'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
		'Sec-Ch-Ua-Mobile': '?0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-User': '?1',
		'Sec-Fetch-Dest': 'document',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
		'Connection': 'close'
	}
#	print(json.dumps(data))
#	return json.dumps(data)
	return data
"""
def solution_capcha(content_capcha):
	RUCAPTCHA_KEY = "2036e78638fb55be1d567dfdb33788ba"
	image_link = content_capcha
	
	user_answer = user_answer = ImageCaptcha.ImageCaptcha(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(captcha_link=image_link)
	
	if not user_answer['error']:
		print(user_answer['captchaSolve'])
		print(user_answer['taskId'])
	elif user_answer['error']:
		print(user_answer['errorBody'])
		print(user_answer['errorBody'])
"""
url = 'https://yandex.ru/search/?lr=56&text={}'.format("смешарики")
wb.open_new_tab(url)


###Response yandex###
headers = req_search_yandex_without_capcha()

http_req = httplib2.Http()
content = http_req.request(url, method = "GET",headers = {'Host': 'yandex.ru',
        'Cookie': 'mda=0; yandex_gid=56; yandexuid=7087684401630933978; yuidss=7087684401630933978',
        'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gec',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close'})[1]

print(content.decode())

#headers = req_search_yandex_without_capcha()
#res_s = requests.get(url, headers = headers)

###################

##response_url = requests.get(url)
##print(response_url.text)
##capcha(response_url.text)
#print(res_s.text)
#list_search = parse_content(res_s.content)
#wb.open_new_tab(list_search[0])
##soup = BeautifulSoup(html_doc)

#print(dir(soup))
