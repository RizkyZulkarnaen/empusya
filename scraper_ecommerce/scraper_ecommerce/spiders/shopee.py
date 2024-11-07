import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.co.id"]
    start_urls = ["https://shopee.co.id/"]

    def parse(self, response):
        pass
