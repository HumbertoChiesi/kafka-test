import httpx
from selectolax.parser import HTMLParser


class MeliScraper:
    def __init__(self):
        self.session = self._create_session()

    def _create_session(self):
        s = httpx.Client()
        return s

    def search(self, query: str) -> HTMLParser:
        """
        Perform a search on Meli and return the HTML content of the search results page

        :param query: The search query
        :return: The HTML content of the Meli search results page
        """
        search_url = "https://www.mercadolivre.com.br/"
        resp = self.session.get(search_url)
        return HTMLParser(resp.text)


scraper = MeliScraper()
print(scraper.search(""))
