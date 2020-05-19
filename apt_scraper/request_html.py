import requests


class RequestHTML:
    def __init__(self, site_label):
        self.site_label = site_label

    def _create_avalon_campbell_url(self, bd):
        url = f"https://www.avaloncommunities.com/california/campbell-apartments/avalon-campbell/apartments?bedroom={str(bd)}BD"

        return url

    def get_html(self, bd):
        if self.site_label == "avalon-campbell":
            url = self._create_avalon_campbell_url(bd)
        request = requests.get(url)

        return request.content

