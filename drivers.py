from selenium import webdriver


def firefox():
    from webdriver_manager.firefox import GeckoDriverManager
    return webdriver.Firefox(executable_path=GeckoDriverManager().install())


def chrome():
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(ChromeDriverManager().install())


def chromium():
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.utils import ChromeType
    return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())


def ie():
    # runs on Windows
    from webdriver_manager.microsoft import IEDriverManager
    return webdriver.Ie(IEDriverManager().install())


def edge():
    # runs on Windows
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    return webdriver.Edge(EdgeChromiumDriverManager().install())


def safari():
    print("Under development")
