from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_browser = webdriver.Chrome('./chromedriver')

print(chrome_browser)