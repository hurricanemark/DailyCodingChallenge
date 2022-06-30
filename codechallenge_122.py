'''
Date: 06/28/2020

Challenge description:
=======================

Controlling the browser with the Selenium module.

'''
from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
type(browser)


browser.get('https://github.com/hurricanemark/')

try:
    elem = browser.find_elements_by_link_text('DailyCodingChallenge')
    type(elem)
    elem.click()
    print('Found <%s> element with the text "DailyCodingChallenge"' % (elem.tag_name))
except Exception as e:
    print(e)
    browser.quit()
    exit()