from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://localhost:8500')

assert 'To-Do' in broser.title

browser.quit()
