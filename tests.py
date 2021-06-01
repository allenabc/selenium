from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
import inspect
import drivers
from fe import *
from selenium.webdriver.common.action_chains import ActionChains


def open_page(page):
    #driver = drivers.firefox()
    driver = drivers.chrome()
    driver.get(page)
    driver.set_window_rect(0, 0, 1300, 1300)
    return driver

def lookup_and_click(driver, xpath):
    el = fe.fe_xpath(driver, xpath)
    if not el:
        driver.close()
        print("element lookup failed")
        return False
    el.click()
    time.sleep(1)
    return True

def cruise_departure():
    driver = drivers.chrome()
    host = "https://www.cruisetimetables.com/"
    driver.get(host)
    driver.set_window_rect(300, 300, 1000, 1000)
    time.sleep(10)


def cruise_time_tabs():
    driver = drivers.chrome()
    host = "https://www.cruisetimetables.com/"
    driver.get(host)
    driver.set_window_rect(300, 300, 1000, 1000)
    anchor = 0
    home = None
    for element in fe.fes_tag_name(driver, 'a'):
        if element.text == "Departure Ports":
            element.click()
            time.sleep(3)
        elif element.text == "Ports of Call":
            element.click()
            time.sleep(3)
        elif element.text == "Cruise Ships":
            element.click()
            time.sleep(3)
        elif element.text == "Home":
            home = element
        anchor += 1
    print("Found {} links".format(anchor))
    home.click()
    time.sleep(1)
    driver.close()


def cruise_time():
    driver = drivers.chrome()
    host = "https://www.cruisetimetables.com/"
    driver.get(host)
    driver.set_window_rect(300, 300, 1000, 1000)
    sale_month = 'sailmonth'  # select pull down
    the_month = 'Dec 2021'  # a choice in pull down
    search_it = 'idCruiseSearch'  # start the search
    destination = 'destination'
    destination_value = "NORTH AMERICA"
    carnival_html = '/cruise-ship-carnival-panorama.html'
    # select a Sail Month and Year
    #Select(fe.fe_id(driver, sale_month)).select_by_value(the_month)
    # select a destination
    #Select(driver.find_element_by_id(drivers, destination)).select_by_value(destination_value)
    # after selecting a sail month start a search
    #fe.fe_id(driver, search_it).click()


def dennys():
    driver = drivers.chrome()
    driver.set_window_rect(0, 0, 1500, 1500)
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": 42.1408845,
        "longitude": -72.5033907,
        "accuracy": 100
    })
    driver.get("https://locations.dennys.com/search.html/")
    time.sleep(1)
    location_icon = driver.find_element_by_css_selector(".icon-geolocate")
    time.sleep(1)
    location_icon.click()
    time.sleep(5)
    print("Geolocation testing with Selenium is complete")


def webcode_me():
    driver = drivers.chrome()
    driver.get("http://webcode.me")
    driver.set_window_rect(0, 0, 1000, 1000)
    assert "My html page" == driver.title
    time.sleep(10)
    driver.close()


def find_elements():
    driver = drivers.chrome()
    driver.get("http://webcode.me")
    driver.set_window_rect(0, 0, 1000, 1000)
    els = driver.find_elements(By.TAG_NAME, "p")
    assert els[0].text == "Today is a beautiful day. We go swimming and fishing."
    assert els[1].text == "Hello there. How are you?"

    for el in els:
        print(el.text)


def g4g_all_links():
    url = "https://www.geeksforgeeks.org"
    driver = open_page(url)
    test_case = inspect.stack()[0].function
    test_result = True
    u = fe.fes_tag_name(driver, 'a')
    try:
        assert len(u) > 400
    except AssertionError:
        print("value to small")
        test_result = False
    finally:
        time.sleep(5)
        driver.close()
    if test_result:
        print("{} passed".format(test_case))
    else:
        print("{} failed".format(test_case))
        exit(1)


def g4g_all_links_with_relpath():
    url = "https://www.geeksforgeeks.org"
    driver = open_page(url)
    test_case = inspect.stack()[0].function
    test_result = True
    u = fe.fes_xpath(driver, "//a")
    z = fe.fes_xpath(driver, "//button")
    u = fe.fes_xpath(driver, "//button[contains(text(),'Got It !')]")
    try:
        assert len(u) < 400
    except AssertionError:
        print("value to small")
        test_result = False
    finally:
        time.sleep(2)
        driver.close()
    if test_result:
        print("{} passed".format(test_case))
    else:
        print("{} failed".format(test_case))
        exit(1)


def shopper_toolkit():
    test_case = inspect.stack()[0].function
    test_result = True
    url='https://www.amazon.com/b/?node=17867753011&ref_=nav_cs_shoppertoolkit_8a71064d19824c0189a2111e6fc0a66f'
    driver = open_page(url)
    xp = "//a[contains(@href,'www.amazon.com/basics')]"
    try:
        u = fe.fe_xpath(driver, xp)
        if u:
            try:
                u.click()
                time.sleep(1)
                assert driver.title == "Amazon.com: Amazonx Basics", "oops failed"
            except:
                print('link to {} failed'.format(u.title))
                test_result = False
        else:
            test_result = False
    except:
        test_result = False
    finally:
        time.sleep(1)
        driver.close()
        if test_result:
            print("{} passed".format(test_case))
        else:
            print("{} failed".format(test_case))
            exit(1)


def g4g_partiaL_link():
    url = "https://www.geeksforgeeks.org"
    driver = open_page(url)
    test_case = inspect.stack()[0].function
    test_result = True
    lnk = "Python Tu"
    title = "Python Programming Language - GeeksforGeeks"
    try:
        u = fe.fe_partial_link_text(driver, lnk)
        if u:
            try:
                u.click()
                time.sleep(2)
                assert driver.title == title
            except:
                print('link to {} failed'.format(u.title))
                test_result = False
        else:
            print("Link >{}< not found".format(lnk))
            test_result = False
    except:
        test_result = False
    finally:
        time.sleep(5)
        driver.close()
        if test_result:
            print("{} passed".format(test_case))
        else:
            print("{} failed".format(test_case))
            exit(1)


def g4g_links():
    url = "https://www.geeksforgeeks.org"
    driver = open_page(url)
    test_case = inspect.stack()[0].function
    test_result = True
    url = "https://www.geeksforgeeks.org"
    test_result = True
    try:
        lnk = "Python Tutorial"
        title = "Python Programming Language - GeeksforGeeks"
        u = fe.fe_link_text(driver, lnk)
        if u:
            try:
                u.click()
                time.sleep(2)
                assert driver.title == title
            except:
                print('link to {} failed'.format(u.title))
                test_result = False
        else:
            print("Link >{}< not found".format(lnk))
            test_result = False
    except:
        test_result = False
    finally:
        time.sleep(5)
        driver.close()
        if test_result:
            print("{} passed".format(test_case))
        else:
            print("{} failed".format(test_case))
            exit(1)


def selenium_easy_demo():
    url = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
    driver = open_page(url)
    test_result = True
    test_case = inspect.stack()[0].function
    sel = '#get-input > .btn'
    page = fe.fe_css_selector(driver, sel)
    tag_name = "button"
    text = 'Show Message'
    try:
        assert page.tag_name == tag_name, "tag name is invalid"
        assert page.text == text, "text value is invalid"
    except AssertionError as e:
        print(e)
        test_result = False
    finally:
        xx = driver.get_full_page_screenshot_as_file("x.png")
        driver.close()
        if test_result:
            print("{} passed".format(test_case))
            exit()
        else:
            print("{} failed".format(test_case))
            exit(1)


def amazon():
    url = "https://www.amazon.com"
    driver = open_page(url)
    test_case = inspect.stack()[0].function
    home_essentials = "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[12]"
    amazon_devices = "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[4]/div/div/a/img"
    tablet = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div[1]/div[3]/div/div/a/img"
    fire_tablet = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div/div[2]/div/ol/li[2]/div/div[1]/a/img"
    tablet_title = "Amazon Fire TV Stick (3rd Gen) with Alexa Voice Remote, Fire Stick Firestick Fire sticks Firesticks, streaming stick"

    time.sleep(3)
    status = lookup_and_click(driver, home_essentials)
    status = lookup_and_click(driver, amazon_devices)
    status = lookup_and_click(driver, tablet)
    status = lookup_and_click(driver, fire_tablet)

    if driver.title == tablet_title:
        print ("{} test passed", test_case)
    driver.close()

def python():
    url = 'https://crossbrowsertesting.github.io/drag-and-drop'
    driver = open_page(url)

    sourceEle = fe_id(driver, "draggable")
    # Store 'box B' as source element
    targetEle = fe_id(driver,"droppable")
    # Performs drag and drop action of sourceEle onto the targetEle
    sleep(9)
    ActionChains(driver).drag_and_drop(sourceEle, targetEle).perform()
    sleep(60)

    driver.close()
