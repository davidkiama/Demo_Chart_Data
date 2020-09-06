from selenium import webdriver
from time import sleep
import pandas as pd


class ChartData:
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('permissions.default.image', 2)
        self.driver = webdriver.Firefox(profile)
        url = "https://www.tradingview.com/symbols/BIST-USDTRYH2021/"
        self.driver.get(url)
        sleep(5)

        #Clicking the 5Y chart
        self.driver.find_element_by_xpath(
            "//div[contains(@class, 'sliderRow-Tv1W7hM5 tabs-1LGqoVz6')]/div[8]"
        ).click()

        chart_name = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[5]/div/header/div/div[2]/div[1]/h1/div[3]'
        ).text
        chart_date = self.driver.find_element_by_css_selector(
            '.js-symbol-lp-time').text
        chart_price = self.driver.find_element_by_css_selector(
            'div.js-symbol-last').text

        #Initilizing
        master_list = []
        data_dict = {}

        data_dict['Chart Name'] = chart_name
        data_dict['Chart Date'] = chart_date
        data_dict['Chart Price'] = chart_price

        master_list.append(data_dict)

        #Saving the data in C.S.V
        df = pd.DataFrame(master_list)
        df.to_csv('Chart_Data.csv', index=False)


ChartData()