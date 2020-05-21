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
        for br in BEDROOMS:
            rh.get_html(site, br)
            rh.save_html(site)
