import os
import pandas
import re
from datetime import datetime
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        pass

    def _get_soup(self, path):
        if os.path.exists(path):
            soup = BeautifulSoup(open(path), "html.parser")

            return soup

    def _parse_info_list(self, soup):
        apt_info_list = soup.find_all("div", {"class": "content"})

        return apt_info_list

    def price_dataframe(self, apt_info_list, path):
        soup = self._get_soup(path)
        apt_info_list = self._parse_info_list(soup)
        data = {
            "Apartment": [],
            "Details": [],
            "Price": [],
            #"Lease Length": [],
            "Availability": [],
            "Parse Date": [],
        }
        for info in apt_info_list:
            apt = info.find("div", {"class": "title brand-main-text-color"}).string
            details = info.find("div", {"class": "title brand-main-text-color"}).string
            price = float(info.find("div", {"class": "price"}).find("span").string.replace("$", ""))
            avail = info.find("div", {"class": "availability"}).string
            date_str = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

