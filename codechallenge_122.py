'''
Date: 06/28/2020

Challenge description:
=======================

Controlling the browser with the Selenium module.

'''
from selenium import webdriver

browser = webdriver.Firefox()
type(browser)


browser.get('https://www.aesclever.com/')