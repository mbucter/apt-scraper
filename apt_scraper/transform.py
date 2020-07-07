from apt_scraper.parser import Parser
import os
import pandas as pd


def transform():
    base_path = "/home/pi/apt-scraper/html"
    files = os.listdir(base_path)
    p = Parser()
    df = pd.DataFrame()
    for file in files:
        split = file.split("_")
        bd = split[2]
        date = split[3]
        year = date[:4]
        month = date[4:6]
        day = date[6:8]
        new_date = f"{month}/{day}/{year}"
        path = os.path.join(base_path, file)
        curr_df = p.price_dataframe(path, new_date, bd)
        df = pd.concat([df, curr_df])

    df.to_csv("/home/pi/apt-scraper/price_data.csv")