from scrapy.crawler import CrawlerProcess
import scrapy
from scrapy.http import FormRequest
from ..items import OrdinaryLevelItem
from scrapy.utils.response import open_in_browser
import json


class OrdinaryLevelSpider(scrapy.Spider):
    name = 'ordinarylevel1'
    number = 10000001
    start_urls = [
        'https://result.doenets.lk/result/service/OlResult?index=10000000&nic=']
    custom_settings = {
        'ITEM_PIPELINES': {'examresults.pipelines.OrdinaryLevelPipeline': 300, }
    }

    def parse(self, response):

        if response.json()['name'] is not None:
            items = OrdinaryLevelItem()

            items['exam'] = response.json()['examination']
            items['year'] = response.json()['year']
            items['name'] = response.json()['name']
            items['indexNo'] = response.json()['indexNo']
            items['nic'] = response.json()['nic']

            items['sub1'] = response.json()['subjectResults'][0]['subjectName']
            items['sub1grade'] = response.json(
            )['subjectResults'][0]['subjectResult']
            items['sub2'] = response.json()['subjectResults'][1]['subjectName']
            items['sub2grade'] = response.json(
            )['subjectResults'][1]['subjectResult']
            items['sub3'] = response.json()['subjectResults'][2]['subjectName']
            items['sub3grade'] = response.json(
            )['subjectResults'][2]['subjectResult']
            items['sub4'] = response.json()['subjectResults'][3]['subjectName']
            items['sub4grade'] = response.json(
            )['subjectResults'][3]['subjectResult']
            items['sub5'] = response.json()['subjectResults'][4]['subjectName']
            items['sub5grade'] = response.json(
            )['subjectResults'][4]['subjectResult']

            items['sub6'] = response.json()['subjectResults'][5]['subjectName']
            items['sub6grade'] = response.json(
            )['subjectResults'][5]['subjectResult']

            items['sub7'] = response.json()['subjectResults'][6]['subjectName']
            items['sub7grade'] = response.json(
            )['subjectResults'][6]['subjectResult']

            items['sub8'] = response.json()['subjectResults'][7]['subjectName']
            items['sub8grade'] = response.json(
            )['subjectResults'][7]['subjectResult']

            items['sub9'] = response.json()['subjectResults'][8]['subjectName']
            items['sub9grade'] = response.json(
            )['subjectResults'][8]['subjectResult']

            yield items

        if OrdinaryLevelSpider.number < 32500000:

            OrdinaryLevelSpider.number += 1

            next_page = 'https://result.doenets.lk/result/service/OlResult?index=' + \
                str(OrdinaryLevelSpider.number) + '&nic='
            yield response.follow(next_page, callback=self.parse)
