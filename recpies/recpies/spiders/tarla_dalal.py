from scrapy import Spider


class AmericanBreakfastSpider(Spider):
    name = "american_breakfast"
    start_urls = [
        "https://www.tarladalal.com/recipes-for-American-Breakfast-136?pageindex=1",
        "https://www.tarladalal.com/recipes-for-American-Breakfast-136?pageindex=2",
        "https://www.tarladalal.com/recipes-for-American-Breakfast-136?pageindex=3",
    ]

    def parse(self, response):
        page = ((response.url.split("/")[-1]).split("?")[-1]).split("=")[-1]
        filename = f"american_breakfast-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
