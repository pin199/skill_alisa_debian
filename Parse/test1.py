from bs4 import BeautifulSoup
import requests
import webbrowser as wb
from urllib.parse import urljoin
from python_rucaptcha import ImageCaptcha
import sys
sys.path.insert(0, "/home/pin/PythonProg/ImageRecognition")
import recim

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
	
	}

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
req_search_yandex_without_capcha()

response_url = requests.get(url)
#print(response_url.text)
capcha(response_url.text)
list_search = parse_content(response_url.content)
wb.open_new_tab(list_search[0])
#soup = BeautifulSoup(html_doc)

#print(dir(soup))
