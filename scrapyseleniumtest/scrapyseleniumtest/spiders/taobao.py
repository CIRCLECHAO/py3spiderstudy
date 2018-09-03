# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from ..items import ProductItem
from scrapy import Spider, Request
from pyquery import PyQuery as pq


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    # start_urls = ['http://www.taobao.com/search?q']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get("MAX_PAGE")+1):
                url = self.base_url + quote(keyword)
                # 不去重
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        doc = pq(response.body)
        ps = doc('#mainsrp-itemlist .items .item').items()
        # print(len(list(ps)))
        for p in ps:
            item = ProductItem()
            image = 'http:' + p.find('.pic .img').attr('data-src')
            price = p.find('.price').text()
            deal = p.find('.deal-cnt').text()
            title = p.find('.title').text()
            shop = p.find('.shop').text()
            location = p.find('.location').text()
            item['image'] = image
            item['price'] = price
            item['deal'] = deal
            item['title'] = title
            item['shop'] = shop
            item['location'] = location

            yield item
