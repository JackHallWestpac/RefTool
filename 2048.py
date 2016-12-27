from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import win32clipboard
from selenium.common.exceptions import NoSuchElementException

Status=True;
#Get Website
# get clipboard data
win32clipboard.OpenClipboard()
ClipBoard = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
    
browser = webdriver.Chrome()
browser.get('http://www.harvardgenerator.com/')

WebSearch = browser.find_element_by_id("website")
WebSearch.clear()
WebSearch.send_keys(ClipBoard)
WebSearch.send_keys(Keys.RETURN)

time.sleep(5)

try:
    Reference = browser.find_element_by_tag_name("blockquote").text
except NoSuchElementException:
  print("invalid website linked copied")
  Status=False

browser.quit()

if Status:
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(Reference)
    win32clipboard.CloseClipboard()
    print(Reference)

