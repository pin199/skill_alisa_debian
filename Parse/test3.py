from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser as wb
from urllib.parse import urljoin
import requests

def req_yand(driver_bw, url):
    driver_bw.get(url)
    return driver_bw.page_source

def parse_sites(get_source):
    soup_main_capcha = BeautifulSoup(get_source, 'html.parser')
    boxes_main_capcha = soup_main_capcha.find_all('a',class_='path__item')
    href_search = []
    for box in boxes_main_capcha:
        try:
            link = box.attrs['href']
            href_search.append(link)
        except:
            pass
    return href_search

def go_site(driver_bw, list_sites):
    driver_bw.get(list_sites[5])
    return driver_bw.page_source

def parse_text_site(get_source):
    soup_go_site = BeautifulSoup(get_source, 'html.parser')
    boxes_go_site = soup_go_site.find_all('p')
    boxes_go_site_main_title = soup_go_site.find('h1').text
    boxes_go_site_title = soup_go_site.find_all('h2')
    list_p = []
    for box in boxes_go_site:
        try:
            link = box.text
            list_p.append(link)
        except:
            pass
#    for box in boxes_go_site_title:
#        link = box.text
    return list_p

def read_text(list_p):
    j = 0
    a = ''
    state_str = ''
    max_count_symbls = 1024
    add_symbl = ''
    for text in list_p:
        for str in enumerate(text):
            if j < max_count_symbls:
                add_symbl += str[1]
                j += 1
            else:
                count = add_symbl.count(' ')
                if str[1] != ' ' and str[1] != '.' and str[1] != '' and str[1] != ',':
                    if a == '':
                        print(a+state_str+' '.join(add_symbl.split(' ')[:-1])) 
                        a =' '.join(add_symbl.split(' ')[count:])
                        print()
                    else:
                        print(a+state_str+' '.join(add_symbl.split(' ')[:-1]))
                        a = ' '.join(add_symbl.split(' ')[count:])
                        print()
                else:
                    print(a+state_str +' '.join(add_symbl.split(' ')[:-1]))
                    a = ' '.join(add_symbl.split(' ')[count:])
                    print()
                state_str = str[1]
                save_state = str[0]
                #Отправить запрос
                #Почистить add_symbl
                add_symbl = ''
                j = 0
def main():
#    path_driver = '/home/pin/git/skill_alisa_debian/Parse/geckodriver'
    driver_bw = webdriver.Safari()
    ####################Request yandex####################
    url = 'https://yandex.ru/search/?lr=56&text={}'.format("ютуб")
    bw_page_source =req_yand(driver_bw, url)
    ####################Parse sites#######################
    list_sites = parse_sites(bw_page_source)
    print(list_sites)
    ###################GoSite#############################
    get_source = go_site(driver_bw, list_sites)
    ###################ParseTextSite######################
    list_parse_text = parse_text_site(get_source)
    print("=====================================")
    print(list_parse_text)
    print("=====================================")
    read_text(list_parse_text)
    ###################ExitDriver######################
    driver_bw.close()

if __name__ == "__main__":
    main()

