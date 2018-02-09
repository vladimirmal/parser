# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.crawler import CrawlerRunner
from scrapy_project.items import QuestionItem
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_project.check_seo import Check

Ch = Check()
class StackoverflowSpider(CrawlSpider):
    name = "stackoverflow"
    start_urls = []
    allowed_domains = []
    url = ''
    rules = (
        Rule(LinkExtractor(allow=url), callback='parse_asd'),
        Rule(LinkExtractor(allow=url), follow=True),
    )

    def parse_asd(self, response):
        item = QuestionItem()
        for quote in response.css('html'):
            counters_anal = quote.css('script').extract()
            if 'https://www.google-analytics.com/analytics.js' in str(counters_anal):
                yee = 'Yes'
            else:
                yee = 'No'
            if 'mc.yandex.ru/metrika' in str(counters_anal):
                res = 'Yes'
            else:
                res = 'No'
            title = quote.css('title::text').extract_first(),

            item['title'] = Ch.check('title', title)
            description = quote.css(
                'meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
            h1 = quote.css('h1::text').extract(),
            h2 = quote.css('h2::text, H2::text').extract(),
            item['description'] = Ch.check('description',description)
            item['h1'] = Ch.check('h1', h1)
            item['h2'] = Ch.check('h2', h2)
            item['keyword'] = quote.css(
                'meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
            item['link'] = response.url
            item['text'] = quote.css('p::text, span::text').extract(),
            item['googl_anal'] = yee,
            item['yandex_metrick'] = res,
            return item

    def start_spider(self, url, short_url):

        self.start_urls.append(url)
        self.allowed_domains.append(short_url)
        self.url = url
        settings = get_project_settings()
        configure_logging(settings=settings)
        runner = CrawlerRunner(settings=get_project_settings())
        d = runner.crawl(StackoverflowSpider)
        d.addCallback(lambda response:reactor.stop())
        reactor.callLater(3, d.addCallback, None)
        reactor.run(installSignalHandlers=0)




