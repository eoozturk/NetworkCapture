import pprint
import time
import unittest

from browsermobproxy import Server
from selenium import webdriver

class ProxyManager:

    __BMP = "Local Path for browsermob proxy\\PycharmProjects\\Test1\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"

    def __init__(self):
        self.__server = Server(ProxyManager.__BMP)
        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):
        self.__client = self.__server.create_proxy(params={"trustAllServers":"true"})
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server

class MtTest(unittest.TestCase):

    proxy = ProxyManager()
    server = proxy.start_server()
    client = proxy.start_client()
    client.new_har("Selenium Har")
    print(client.proxy)

    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server={}".format(client.proxy))
    driver = webdriver.Chrome("Local Path\\PycharmProjects\\Test1\\chromedriver.exe", chrome_options=options)
    driver.maximize_window()
    driver.delete_all_cookies()
    '''
    Browser Cache Delete   
    driver.get("chrome://settings/clearBrowserData")
    clearButton = driver.find_element_by_css_selector("* /deep/ #clearBrowsingDataConfirm")
    wait = WebDriverWait(driver, 60)
    wait.until(clearButton)
    clearButton.click()
    wait.until_not(clearButton)
    '''
    driver.get("Your Test URL")
    time.sleep(7)

    '''Selenium Test Adımları:'''
    # Login & MT Ekranına Giriş
    driver.find_element_by_id("email").send_keys(" ")
    driver.find_element_by_id("password").send_keys(" ")
    driver.save_screenshot("Selenium1.png")
    driver.find_element_by_class_name("MuiButton-label").click()
    time.sleep(5)

    driver.find_element_by_id("home-aMusteri").click()
    driver.save_screenshot("Selenium2.png")
    driver.find_element_by_class_name("ui-dialog-buttonset").click()
    time.sleep(10)

    #driver.switch_to.active_element()
    '''Status Değişiklikleri'''
    ready = driver.find_element_by_id("agent-status-available")
    ready.click()
    driver.save_screenshot("Selenium3.png")
    time.sleep(3)
    sbreak = driver.find_element_by_id("agent-status-shortbreak")
    sbreak.click()
    time.sleep(3)
    lunch = driver.find_element_by_id("agent-status-lunch")
    lunch.click()
    driver.save_screenshot("Selenium4.png")
    time.sleep(3)
    train = driver.find_element_by_id("agent-status-training")
    train.click()
    time.sleep(3)
    meet = driver.find_element_by_id("agent-status-meeting")
    meet.click()
    time.sleep(3)
    acw = driver.find_element_by_id("agent-status-acw")
    acw.click()
    driver.save_screenshot("Selenium5.png")
    time.sleep(3)
    try:
        harFile = open("harFile.txt","w+")
        harFile.write(client.har)
        harFile.close()
    except:
        pprint.pprint(client.har)

    driver.close()
    server.stop()

if __name__ == "__main__" :
    unittest.main()
