import scrapy
from ..items import BayutItem


class BayutSpider(scrapy.Spider):
    page_num=55
    name = "homes"
    start_urls = [f'https://www.bayut.jo/%D8%B5%D9%81%D8%AD%D8%A9-55/%D9%81%D9%84%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%B9%D9%85%D8%A7%D9%86/?price_min=1000&price_max=1000000']

    def parse(self, response):
        item = BayutItem()
        no_content = response.css("span._5264eceb::text").extract()
        if not no_content :
            home_cards = response.css('li.ef447dde')
            for card in home_cards:

                price = card.css('span.f343d9ce::text').extract()
                space = card.css('span[aria-label="Area"] span._4bdd430c::text').extract()
                city_and_region = card.css('div._00a37089::text').extract()
                path_rooms = card.css('span[aria-label="Baths"]::text').extract()
                sleep_rooms = card.css('span[aria-label="Beds"]::text').extract()

                item['price'] = price
                item['space'] = space
                item['city_and_region'] = city_and_region
                item['path_rooms'] = path_rooms
                item['sleep_rooms'] = sleep_rooms

                yield item



            BayutSpider.page_num += 1
            next_page = f'https://www.bayut.jo/%D8%B5%D9%81%D8%AD%D8%A9-{BayutSpider.page_num}/%D9%81%D9%84%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%B9%D9%85%D8%A7%D9%86/?price_min=1000&price_max=1000000'
            # no_content = response.css("span._5264eceb::text").extract()
            yield response.follow(next_page, callback=self.parse)










