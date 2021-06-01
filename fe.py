from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import drivers

# Selenium or Appium

def open_page(page):
    #driver = drivers.firefox()
    driver = drivers.chrome()
    driver.get(page)
    driver.set_window_rect(0, 0, 1300, 1300)
    return driver

def fe_id(driver, myid):
    try:
        return driver.find_element(By.ID, myid)
    except:
        return False


def fe_name(driver, t):
    try:
        return driver.find_element(By.NAME, t)
    except:
        return False
""" 
element by tag name
finds first tag of that type
Fails with NoSuchElementException
driver.find_element_by_tag_name('h1')
"""


def fe_xpath(driver, xp):
    """"
    XPath stands for XML Path Language
    XPath uses "path like" syntax to identify and navigate nodes in an XML document
    """
    try:
        return driver.find_element(By.XPATH, xp)
    except:
        return False


def fe_link_text(driver, lnk):
    """
    Find a href= term and extract text
    """
    try:
        return driver.find_element(By.LINK_TEXT, lnk)
    except:
        return False


def fe_partial_link_text(driver, txt):
    try:
        return driver.find_element(By.PARTIAL_LINK_TEXT, txt)
    except:
        return False


def fe_tag(driver, tag):
    try:
        driver.find_element(By.TAG_NAME, value='a')
    except:
        return False


def fe_class_name(driver, aclass):
    try:
        return driver.find_element(By.CLASS_NAME, aclass)
    except:
        return False


def fe_css_selector(driver, css):
    try:
        return driver.find_element(By.CSS_SELECTOR, css)
    except:
        return False

# Plural
# Provide list of objects
def fes_name(driver, name):
    try:
        return driver.find_elements(By.NAME, name)
    except:
        return False


def fes_xpath(driver, xpath):
    try:
        return driver.find_elements(By.XPATH, xpath)
    except:
        return False


def fes_link_text(driver, lnk):
    try:
        return driver.find_elements(By.LINK_TEXT, lnk)
    except:
        return False


def fes_partial_link_text(driver, txt):
    try:
        return driver.find_elements(By.PARTIAL_LINK_TEXT, txt)
    except:
        return False


def fes_tag_name(driver, tag):
    try:
        return driver.find_elements(By.TAG_NAME, tag)
    except:
        return False


def fes_class_name(driver, my_class):
    try:
        return driver.find_elements(By.CLASS_NAME, my_class)
    except:
        return False


def fes_css_selector(driver, sel):
    try:
        return driver.find_elements(By.CSS_SELECTOR, sel)
    except:
        return False

# Locators
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# locate by Name
# find_elements_by_name
#   <input name="continue" type="submit" value="Login" />
#   driver.find_element_by_name(“continue”)

# locate by Xpath
# find_elements_by_xpath

# Nodes
# Element
# Attribute
# Text
# Namespace
# Processing-instruction
# Comment
# Document


# find_elements_by_link_text
# OR
# find_elements_by_partial_link_text
#
#   <a href="continue.html">Continue</a>
#   <a href="cancel.html">Cancel</a>
#
#   continue_link = driver.find_element_by_link_text('Continue')
#   continue_link = driver.find_element_by_partial_link_text('Conti')

#

# Find by tag
# find_elements_by_tag_name
#   heading1 = driver.find_element_by_tag_name('h1')

# find_elements_by_class_name
#    <p class="content">Site content goes here.</p>
#    content = driver.find_element_by_class_name('content')

# find_elements_by_css_selector
#    <p class="content">Site content goes here.</p>
#    content = driver.find_element_by_css_selector('p.content')

# Cookies

#       https://celestialsys.com/blog/web-automation-with-selenium-webdriver-using-python-part-2/