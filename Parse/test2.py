from bs4 import BeautifulSoup
from selenium import webdriver
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
def read_text(list_p):
# Нужно обрезать текст по точке или по правому входящему
    i = 0
    j = 0
    a = ''
    state_str = ''
#    count_symbls
    max_count_symbls = 1024
    add_symbl = ''
    for text in list_p:
        for str in enumerate(text):
            if j < max_count_symbls:
                add_symbl += str[1]
                j += 1
#                print(j)
#                print(str[1])
            else:
                print("###################################")
                print(str[1])
                print("###################################")
                if str[1] != ' ' or str[1] != '.' or str[1] != '' or str[1] != ',':
                    # вырезать слова из текста
                    count = add_symbl.count(' ') 
                    print("----------------------------------")
                    print(a)
                    print("----------------------------------")
                    if a == '':
                        print(' '.join(add_symbl.split(' ')[:-1]))
                        a = ' '.join(add_symbl.split(' ')[count:])
                    else:
#                        a = ' '.join(add_symbl.split(' ')[count:])
                        print(a+state_str+' '.join(add_symbl.split(' ')[:-1]))
                        a = ' '.join(add_symbl.split(' ')[count:])
                state_str = str[1]
			    #Learn long max str
                save_state = str[0]
#                print(save_state)
                #Отправить запрос
 #               print(add_symbl)
                #Почистить add_symbl
                add_symbl = ''
                j = 0
        i += 1
        
"""
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

def search_string_retpath(string):
	index_begin = string.find("retpath") +  8
	index_end = string.find("&", index_begin)
#	print(index_begin)
#	print(index_end)
	i = 0
	str_url = ""
	for str in enumerate(string):
#		print(str)
#		print(str[0])
		if i == index_begin or (i > index_begin and i < index_end):
#			print(i)
			str_url = str_url + str[1]
		i += 1
#	print(str_url)
	return str_url

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

url = 'https://yandex.ru/search/?lr=56&text={}'.format("ютуб")
#wb.open_new_tab(url)


###Response yandex###
#headers = req_search_yandex_without_capcha()

http_req = httplib2.Http()
content = http_req.request(url, method = "GET",headers = {'Host': 'yandex.ru',
        'Cookie': 'mda=0; yandex_gid=56; yandexuid=7087684401630933978; yuidss=7087684401630933978',
        'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Safari/537.36 AppleWebKit/537.36 (KHTML, like Gec',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close'})[1]
soup_capcha = BeautifulSoup(content, 'html.parser')
boxes_capcha = soup_capcha.find('div', class_='CheckboxCaptcha')
boxes_capcha_t = boxes_capcha.find('form').attrs['action']
boxes_capcha = boxes_capcha_t
boxes_search_string_retpath = search_string_retpath(boxes_capcha)
#print("==============================")
#print(boxes_capcha)
#print(str(search_string_retpath(boxes_capcha)))
#print(1)
#print("==============================")

#print("==============================")
 
url_capcha = 'https://yandex.ru'+ boxes_capcha
http_req_capcha = httplib2.Http()
capcha_content = http_req_capcha.request(url_capcha,method = "GET",headers= {
	'Host': 'yandex.ru',
	'Cookie': 'mda=0; yandex_gid=56; yandexuid=7087684401630933978; yuidss=7087684401630933978; is_gdpr=0; is_gdpr_b=CLPnPBCARCgC; font_loaded=YSv1; ymex=1946294093.yrts.1630934093; _ym_uid=1630934123448513266; my=YwA=; _ym_d=1631103399; i=QoWLSC0mIWmloSGIeHN3MUlYbIAkedOneZ8Cjq3IdMeLq7VKZU4zxYTSJIlEcHLa0B2ho62CGKIf692aEX56Xcz3jtg=; spravka=dD0xNjMyNTc0ODQ1O2k9NzcuMjIyLjEwNy44O0Q9RjVCMEM2QkVEQzc1Rjg1NDc4MTA2RkQ2MDkwMUI0NTJGM0MwMThEN0ZDQjM1QTJGQzkzQzVFOTY3RkFDOTk1Q0U0NDA7dT0xNjMyNTc0ODQ1MTg1MjE0NDUxO2g9NmU4NjBkZDM3OGE3NmQ3MDZlOGIxZGJkZDA2NDYyZmQ=; yabs-frequency=/5/0000000000000000/bUDqs4l_UKpqGa3QagJCGnBgSlH28000/; yp=1633525979.ygu.1#1646702097.szm.1:1440x900:911x707#1633781776.csc.1#1664110856.p_sw.1632574855#1633179014.mcv.0#1633179014.mct.null#1633179014.mcl.; _yasc=jw6emxxhLoSlYCEWvt+1qnuATGtUWNj0nT5PwvWWPwQ/OgB9LjKpjw==',
	'Sec-Ch-Ua': '"Chromium";v="93", " Not;A Brand";v="99"',
	'Sec-Ch-Ua-Mobile': '?0',
	'Sec-Ch-Ua-Platform': '"macOS"',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-User': '?1',
	'Sec-Fetch-Dest': 'document',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
	'Connection': 'close'
})[1]

#soup_check_capcha = BeautifulSoup(capcha_content,'html.parser')
#boxes_check_capcha = soup_check_capcha.find('form', class_='AdvancedCaptcha-Form').attrs['action']
#print('-------------------------------------')
#print(capcha_content['location'])
#print(boxes_check_capcha)
#print(capcha_content.getheaders())
#print('-------------------------------------')

"""
url_check_capcha = '/checkcaptcha?key=00Aa8x4LReWmhyTKSD4QzlWn6ck3qzVC_3%2F1632662498%2Ffa57d6f4db4c9a337822795ceba5cf83_07024daa9f4107e6e920a144bccb7b43&retpath=https%3A%2F%2Fyandex.ru%2Fsearch%3Flr%3D56%26text%3D%25D1%2581%25D0%25BC%25D0%25B5%25D1%2588%25D0%25B0%25D1%2580%25D0%25B8%25D0%25BA%25D0%25B8_f7638bef21a6e08dd809d7942c1c1c86&u=9c926652-b4d58985-9529d41f-a2027be3&rep=%D0%BF%D0%BE%D0%BA%D0%B8%D0%B4%D0%B0%D1%8E%20%D0%BF%D0%BE%D1%81%D0%B5%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D0%B5'
"""

url_check_capcha = '/checkcaptcha?key=00Aa8x4LReWmhyTKSD4QzlWn6ck3qzVC_3%2F1632662498%2Ffa57d6f4db4c9a337822795ceba5cf83_07024daa9f4107e6e920a144bccb7b43&retpath='+ boxes_search_string_retpath +'&u=9c926652-b4d58985-9529d41f-a2027be3&rep=%D0%BF%D0%BE%D0%BA%D0%B8%D0%B4%D0%B0%D1%8E%20%D0%BF%D0%BE%D1%81%D0%B5%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D0%B5'
#url_check_capcha = boxes_check_capcha



url_capcha_main = 'https://yandex.ru'+ url_check_capcha
http_req_capcha_main = httplib2.Http()
capcha_main_content = http_req_capcha_main.request(url_capcha_main, method = "POST", headers = {
	'Host': 'yandex.ru',
	'Content-Length': '1511',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'Origin': 'http://yandex.ru',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Referer': 'http://yandex.ru/showcaptcha?retpath=https%3A//yandex.ru/search%3Flr%3D56%26text%3D%25D1%2581%25D0%25BC%25D0%25B5%25D1%2588%25D0%25B0%25D1%2580%25D0%25B8%25D0%25BA%25D0%25B8_f7638bef21a6e08dd809d7942c1c1c86&t=3/1632662498/fa57d6f4db4c9a337822795ceba5cf83&u=9c926652-b4d58985-9529d41f-a2027be3&s=5390fb6d8acdb4feccf3548aef9b7c4b',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
	'Cookie': 'mda=0; font_loaded=YSv1; spravka=dD0xNjMyNTc0ODQ1O2k9NzcuMjIyLjEwNy44O0Q9RjVCMEM2QkVEQzc1Rjg1NDc4MTA2RkQ2MDkwMUI0NTJGM0MwMThEN0ZDQjM1QTJGQzkzQzVFOTY3RkFDOTk1Q0U0NDA7dT0xNjMyNTc0ODQ1MTg1MjE0NDUxO2g9NmU4NjBkZDM3OGE3NmQ3MDZlOGIxZGJkZDA2NDYyZmQ=; yp=1633525979.ygu.1#1646702097.szm.1:1440x900:911x707#1633781776.csc.1#1664110856.p_sw.1632574855#1633179014.mcv.0#1633179014.mct.null#1633179014.mcl.; gdpr=0; _ym_visorc=b',
	'Connection': 'close'
})[0]
#print(capcha_main_content.decode())
#soup_main_capcha = BeautifulSoup(capcha_main_content, 'html.parser')
#boxes_main_capcha = soup_main_capcha.find('div',class_='organic__url-text')
#print(boxes_main_capcha)
#print("++++++++++++++++++++++++++++++++++")
#print(capcha_main)
#print("++++++++++++++++++++++++++++++++++")
url_yan = capcha_main_content['location']
#http_req_main_capcha = httplib2.Http()
#content_req_main = http_req_main_capcha.request(url_yan,method="GET")[1]
#print(content_req_main.decode())
driver_bw = webdriver.Safari()
driver_bw.get(url_yan)
get_source = driver_bw.page_source

soup_main_capcha = BeautifulSoup(get_source, 'html.parser')
boxes_main_capcha = soup_main_capcha.find_all('a',class_='path__item')
#print(boxes_main_capcha)
href_search = []
for box in boxes_main_capcha:
    try:
#        link = box.find('a', class_='path__item').attrs['href']
        link = box.attrs['href']
#        print(link)
        href_search.append(link)
    except:
        pass
#print(href_search)
#    print(link)
#print(get_source)

################GoSite###################
driver_bw.get(href_search[5])
get_source = driver_bw.page_source
#print(get_source)
soup_go_site = BeautifulSoup(get_source, 'html.parser')
boxes_go_site = soup_go_site.find_all('p')
boxes_go_site_main_title = soup_go_site.find('h1').text
boxes_go_site_title = soup_go_site.find_all('h2')
#print(boxes_go_site)
list_p = []
for box in boxes_go_site:
    try:
        link = box.text
#        print(link)
        list_p.append(link)
    except:
        pass
#print(boxes_go_site_main_title)
for box in boxes_go_site_title:
    link = box.text
#    print(link)
#print(boxes_go_site)
#print('+++++++++++++++++++++++++++++++++++++++++++++++')
read_text(list_p)

driver_bw.close()

#url_yan = capcha_content['location']
#wb.open_new_tab(url_yan)

"""
print(content.decode())
print('=============================================')
print(capcha_content.decode())
print('=============================================')
print('1')
print(capcha_main_content.status)
print(capcha_main_content['location'])
"""
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
