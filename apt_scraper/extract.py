from time import sleep
from apt_scraper.request_html import RequestHTML


BEDROOMS = [
    1,
    2,
]

SITES = [
    "avalon-campbell",
]

def extract():
    rh = RequestHTML()
    for site in SITES:
        for bd in BEDROOMS:
            rh.get_html(site, bd)
            rh.save_html(site, bd)
            sleep(1.5)
