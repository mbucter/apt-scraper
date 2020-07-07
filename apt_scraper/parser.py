import os
import pandas as pd
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

    def price_dataframe(self, path, date, bd):
        soup = self._get_soup(path)
        apt_info_list = self._parse_info_list(soup)
        data = []
        for info in apt_info_list:
            row = {}
            apt = info.find("div", {"class": "title brand-main-text-color"}).string
            details = info.find("div", {"class": "title brand-main-text-color"}).string
            price = float(info.find("div", {"class": "price"}).find("span").string.replace("$", "").replace(",", ""))
            avail = info.find("div", {"class": "availability"}).string
            #date_str = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            row["Apartment"] = apt
            row["Details"] = details
            row["Price"] = price
            row["Availability"] = avail
            row["Date"] = date
            row["Bedrooms"] = bd
            data.append(row)

        return pd.DataFrame(data)
