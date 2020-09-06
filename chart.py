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
            "//div[contains(@class, 'tabs-1LGqoVz6')]/div[8]").click()

        exchange_symbol = self.driver.find_element_by_xpath(
            "//*[@id='anchor-page-1']/div/div[2]/div[1]/h1/div[2]").text

        chart_name = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[5]/div/header/div/div[2]/div[1]/h1/div[3]"
        ).text

        chart_date = self.driver.find_element_by_css_selector(
            ".js-symbol-lp-time").text

        chart_price = self.driver.find_element_by_css_selector(
            "div.js-symbol-last").text

        prev_close = self.driver.find_element_by_xpath(
            "//*[@id='anchor-page-1']/div/div[3]/div[3]/div[1]/div[1]").text

        open_price = self.driver.find_element_by_xpath(
            "//*[@id='anchor-page-1']/div/div[3]/div[3]/div[2]/div[1]"
        ).text.strip()

        volume = self.driver.find_element_by_xpath(
            "//*[@id='anchor-page-1']/div/div[3]/div[3]/div[3]/div[1]"
        ).text.strip()

        days_range = self.driver.find_element_by_xpath(
            "//*[@id='anchor-page-1']/div/div[3]/div[3]/div[4]/div[1]/div"
        ).text.strip()

        #Initilizing
        master_list = []
        data_dict = {}

        data_dict['Exchange Symbol'] = exchange_symbol
        data_dict['Chart Name'] = chart_name
        data_dict['Chart Date'] = chart_date
        data_dict['Chart Price'] = chart_price
        data_dict['Prev Close'] = prev_close
        data_dict['Open Price'] = open_price
        data_dict['Volume'] = volume
        data_dict['Day\'s Range'] = days_range

        master_list.append(data_dict)

        #Saving the data in C.S.V
        df = pd.DataFrame(master_list)
        df.to_excel('Chart_Data.xlsx', index=False, engine='xlsxwriter')


ChartData()