import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from vinpromkarnobat.items import Article


class VinpromSpider(scrapy.Spider):
    name = 'vinprom'
    allowed_domains = ['vinpromkarnobat.bg']
    start_urls = ['http://vinpromkarnobat.bg/%D0%9D%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8.htm']

    def parse(self, response):
        articles = response.xpath("//ul/li/a/@href").getall()
        yield from response.follow_all(articles, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath("//h1/text()").get()
        title = title.replace('"', "'")
        content = response.xpath("//div[@id='align-center']//p//text()").getall()
        content = " ".join(content)
        content = content.replace('"', "'")

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
