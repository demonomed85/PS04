from selenium import webdriver
from urllib.parse import urlencode
from selenium.webdriver.common.by import By

request = input('Введите запрос: ')
browser = webdriver.Firefox()
base_ulr = "https://ru.wikipedia.org/w/index.php?"
params = {'search': request}

url = f'{base_ulr}{urlencode(params)}'

browser.get(url)
print ('\nГлавное меню:')
while True:
    key = input('"p" - получения парагафа\n"l" - получения ссылок\n"q" - выход: ')
    if key == 'q':
       break
    elif key == 'p':
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        for paragraph in paragraphs:
            print(paragraph.text)
            key =input('Нажмите Enter для продолжения или q для выхода в главное меню: ')
            if key == 'q':
                print('\nГлавное меню:')
                break
    elif key == 'l':
        external_links = []

        links_section = browser.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/ul[6]')

        links = links_section.find_elements(By.TAG_NAME, 'a')

        link_num = 1
        for link in links:
            link_text = link.text
            link_url = link.get_attribute('href')
            print(f'{link_num} {link_text}, {link_url}')
            external_links.append(link.get_attribute('href'))
            link_num += 1


        key =input('Укажите номер ссылки или q для выхода в главное меню: ')

        if int(key) > 0 and int(key) <= len(external_links):
           browser.get(external_links[int(key)-1])
        elif key == 'q':
           print('\nГлавное меню:')
           break


browser.quit()