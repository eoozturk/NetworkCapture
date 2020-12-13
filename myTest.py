import pprint

from browsermobproxy import Server
from selenium import webdriver
import time

class ProxyManager:

    __BMP = "C:\\Users\\AloTech\\PycharmProjects\\Test1\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"

    def __init__(self):
        self.__server = Server(ProxyManager.__BMP)
        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):

        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server

if "__main__" == __name__:

    proxy = ProxyManager()
    client = proxy.start_client()
    server = proxy.start_server()
    client.new_har("google.com")

    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server:{}".format(client.proxy))
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://google.com.tr/")
    time.sleep(5)

    pprint.pprint(client.har)

    server.stop()






