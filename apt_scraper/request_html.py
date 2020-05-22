import os
import requests
from datetime import datetime


class RequestHTML:
    def __init__(self):
        self.html = None

    def _create_avalon_campbell_url(self, bd):
        url = f"https://www.avaloncommunities.com/california/campbell-apartments/avalon-campbell/apartments?bedroom={str(bd)}BD"

        return url

    def _ensure_dirs(self, top_dir):
        apt_dir = os.path.join(top_dir, "apt-scraper")
        html_dir = os.path.join(apt_dir, "html")
        if not os.path.exists(apt_dir):
            os.makedirs(apt_dir)
        if not os.path.exists(html_dir):
            os.makedirs(html_dir)

    def get_html(self, site_label, bd=""):
        if site_label == "avalon-campbell":
            url = self._create_avalon_campbell_url(bd)
        request = requests.get(url)
        self.html = request.text

        return self.html

    def save_html(self, site_label, bd=""):
        home = os.path.expanduser("~")
        self._ensure_dirs(home)
        html_out_path = os.path.join(home, "apt-scraper/html")
        date_str = datetime.now().strftime("%Y%m%d%H%M%S")
        fn = os.path.join(html_out_path, f"apt_{site_label}_{bd}_{date_str}.html")
        if self.html:
            txt = open(fn, "w", encoding="utf-8")
            txt.write(self.html)
            txt.close()
