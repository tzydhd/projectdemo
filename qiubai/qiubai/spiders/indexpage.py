import scrapy
from scrapy.http import request
from qiubai.items import QiubaiItem

class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls=["http://www.qiushibaike.com/",]
    def parse(self,response):
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        #print(response.xpath('//div[@class="content"]').extract())
        for ele in response.xpath('//div[@class = "article block untagged mb15 typs_long"]'):
            authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            contents =ele.xpath('./a[1]/div[@class="content"]/span/text()').extract
            yield QiubaiItem(author=authors, content=contents)