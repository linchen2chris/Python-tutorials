import scrapy


class DailyFundSpider(scrapy.Spider, fundNum='003096'):
    name = "dailyFound"
    start_urls = ['http://fund.eastmoney.com/%s.html?spm=search' % fundNum]

        for article in response.xpath('//*[@id="gz_gszzl"]')
    def parse(self, response):
