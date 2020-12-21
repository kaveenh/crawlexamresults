from scrapy.crawler import CrawlerProcess
import scrapy
from scrapy.http import FormRequest
from ..items import ScholarshipItem
from scrapy.utils.response import open_in_browser
import json


class ScholarshipSpider(scrapy.Spider):
    name = 'scholarship3'
    number = 5500001
    start_urls = ['https://result.doenets.lk/result/service/GvResult/5500000']
    custom_settings = {
        'ITEM_PIPELINES': {'examresults.pipelines.ScholarshipPipeline': 300, }
    }

    def parse(self, response):

        if response.json()['name'] is not None:
            items = ScholarshipItem()

            items['exam'] = response.json()['examination']
            items['year'] = response.json()['year']
            items['indexNo'] = response.json()['indexNo']
            items['name'] = response.json()['name']
            items['marks'] = response.json()['marks']

            yield items

        if ScholarshipSpider.number < 7750000:

            ScholarshipSpider.number += 1

            next_page = 'https://result.doenets.lk/result/service/GvResult/' + \
                str(ScholarshipSpider.number) + '/'
            yield response.follow(next_page, callback=self.parse)
