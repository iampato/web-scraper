from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class WebCrawler:
    # url: the url to be crawled
    # driver: the driver to be used
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    # crawl: crawl the url
    def crawl(self):
        self.driver.get(self.url)
        # get radio button with id 'PDI_answer51183277'
        radio_button = self.driver.find_element(
            by=By.ID,
            value='PDI_answer51183277'
        )
        # click the radio button
        radio_button.click()
        # get the submit button
        submit_button = self.driver.find_element(
            by=By.ID,
            value='pd-vote-button11192515'
        )
        # click the submit button
        submit_button.click()
        return self.driver.page_source

    def cleanCookies(self):
        self.driver.delete_all_cookies()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    url = "https://poll.fm/11192515"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    crawler = WebCrawler(url, driver)
    # crawler.crawl()
    # crawler.cleanCookies()
    # range 1 to 100
    for i in range(1, 101):
        try:
            ## crawl the url
            crawler.crawl()
            ## clean cookies
            crawler.cleanCookies()
            print("Crawled {} times".format(i))
            time.sleep(2)
        except Exception as e:
            print(e)

    crawler.close()
