from selenium.webdriver.support.ui import Select
import inspect
import drivers
from fe import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from drivers import firefox, chrome, chromium, ie, edge
from selenium import webdriver
from selenium.webdriver.common.by import By

def start(host):
    driver = chrome()
    # Navigate to url
    driver.get(host)
    driver.set_window_rect(200, 200, 1000, 1000)
    return driver

def click_hold():
    host = "http://www.google.com"
    driver = start(host)
# Store 'google search' button web element
    searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")
# Perform click-and-hold action on the element
    webdriver.ActionChains(driver).click_and_hold(searchBtn).perform()
    sleep(60)

def context_click():
    host = "http://www.google.com"
    driver = start(host)     # Store 'google search' button web element
    searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")
# Perform context-click action on the element
    webdriver.ActionChains(driver).context_click(searchBtn).perform()
    sleep(60)

def double_click():
    host = "http://www.google.com"
    driver = start(host)     # Store 'google search' button web element
    # Store 'google search' button web element
    searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")
    # Perform double-click action on the element
    webdriver.ActionChains(driver).double_click(searchBtn).perform()
    sleep(60)

def move_to_element():
    host = "http://www.google.com"
    driver = start(host)
    # Store 'google search' button web element
    gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")
    # Performs mouse move action onto the element
    webdriver.ActionChains(driver).move_to_element(gmailLink).perform()
    sleep(60)

def move_by_offset():
    host = "http://www.google.com"
    driver = start(host)
    # Store 'google search' button web element
    gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")
    # Set x and y offset positions of element
    xOffset = 100
    yOffset = 100
    # Performs mouse move action onto the element
    webdriver.ActionChains(driver).move_by_offset(xOffset, yOffset).perform()
    sleep(60)

def drag_and_drop():
    host = "https://crossbrowsertesting.github.io/drag-and-drop"
    driver = start(host)
    # Store 'box A' as source element
    sourceEle = driver.find_element(By.ID, "draggable")
    # Store 'box B' as source element
    targetEle = driver.find_element(By.ID, "droppable")
    # Performs drag and drop action of sourceEle onto the targetEle
    webdriver.ActionChains(driver).drag_and_drop(sourceEle, targetEle).perform()
    sleep(60)

def drag_and_drop_by():
    host = "https://crossbrowsertesting.github.io/drag-and-drop"
    driver = start(host)
    # Store 'box A' as source element
    sourceEle = driver.find_element(By.ID, "draggable")
    # Store 'box B' as source element
    targetEle = driver.find_element(By.ID, "droppable")
    targetEleXOffset = targetEle.location.get("x")
    targetEleYOffset = targetEle.location.get("y")

    # Performs dragAndDropBy onto the target element offset position
    webdriver.ActionChains(driver).drag_and_drop_by_offset(sourceEle, targetEleXOffset, targetEleYOffset).perform()
    sleep(60)

def release():
    host = "https://crossbrowsertesting.github.io/drag-and-drop"
    driver = start(host)
    # Store 'box A' as source element
    sourceEle = driver.find_element(By.ID, "draggable")
    # Store 'box B' as source element
    targetEle = driver.find_element(By.ID, "droppable")

    # Performs dragAndDropBy onto the target element offset position
    webdriver.ActionChains(driver).click_and_hold(sourceEle).move_to_element(targetEle).perform()
    # Performs release event
    webdriver.ActionChains(driver).release().perform()
    sleep(60)

