# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy import Spider, Request
import json
from ..items import ImageItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {'ch': 'beauty', 'listtype': 'new'}
        base_url = 'https://images.so.com/zj?'
        for page in range(1, self.settings.get("MAX_PAGE") + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            # 不返回生成器 大家都很难做
            yield item
