from requests_html import HTMLSession


class Scraper():
    def scrape_data(self, tag):
        url = f"https://quotes.toscrape.com/tag/{tag}"
        s = HTMLSession()   
        r = s.get(url)
        print(r.status_code)

        quotes_list = []

        quotes = r.html.find("div.quote")

        for quote in quotes:
            item = {
                "text": quote.find("span.text", first=True).text,
                "author": quote.find("small.author", first=True).text,
                "tags": quote.find("div.tags a.tag", first=True).text
            }
            quotes_list.append(item)
        
        return quotes_list

quotes = Scraper()

quotes.scrape_data("life")