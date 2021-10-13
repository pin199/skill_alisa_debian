from selenium import webdriver
import webbrowser as wb
from urllib.parse import urljoin
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

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

#def read_text_last:
    

def read_text(list_p):
    j = 0
    a = ''
    i = 0
    state_str = ''
    max_count_symbls = 1000
    add_symbl = ''
    state_cycle = 0
#######State lasr text#########
    state_last_text = ''
    for text in list_p:
#        print("************************************")
#        print(text)
#        print("************************************")
        for str in enumerate(text):
            if j < max_count_symbls:
                add_symbl += str[1]
                j += 1
            else:
#                print('j:',j)
#                print(str[1])
                count = add_symbl.count(' ')
                if str[1] != ' ' and str[1] != '.' and str[1] != '' and str[1] != ',':
                    if a == '':
                        print(a+state_str+' '.join(add_symbl.split(' ')[:-1]))
                        state_last_text = a + state_str + ' '.join(add_symbl.split(' ')[:-1]) 
                        a =' '.join(add_symbl.split(' ')[count:])
                        print()
                    else:
                        print(a+state_str+' '.join(add_symbl.split(' ')[:-1]))
                        state_last_text = a + state_str + ' '.join(add_symbl.split(' ')[:-1])
                        a = ' '.join(add_symbl.split(' ')[count:])
                        print()
                else:
                    print(a+state_str +' '.join(add_symbl.split(' ')[:-1]))
                    state_last_text = a + state_str + ' '.join(add_symbl.split(' ')[:-1])
                    a = ' '.join(add_symbl.split(' ')[count:])
                    print()
#                state_last_text = a + state_str + ' '.join(add_symbl.split(' ')[:-1])
                state_str = str[1]
                save_state = str[0]
                state_cycle = i
                #Отправить запрос
                #Почистить add_symbl            
                add_symbl = ''
                j = 0 
        i+=1
    k = state_cycle
    y = 0
    add_symbl_last = ''
    count_last_text = 0 
    count_last_text = state_last_text.count(' ')
    cut_last_text = ' '.join(state_last_text.split(' ')[count_last_text:])
#    for str in list_p[i]:
        
        
    if i - state_cycle > 0:
        while k < i:
            for string in enumerate(list_p[k]):
                y+=1
            if y < max_count_symbls:
                add_symbl_last += string[1]
            print(y)
            if y < max_count_symbls:
                print(list_p[k])
#            else:
                
                                    

def main():
#    path_driver = '/usr/bin/safaridriver'
#   executable_path
    driver_bw = webdriver.Chrome(ChromeDriverManager().install())
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

