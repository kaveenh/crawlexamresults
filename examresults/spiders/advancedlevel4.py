from scrapy.crawler import CrawlerProcess
import scrapy
from scrapy.http import FormRequest
from ..items import AdvancedLevelItem
from scrapy.utils.response import open_in_browser
import json


class AdvancedLevelSpider(scrapy.Spider):
    name = 'advancedlevel4'
    number = 7750001
    start_urls = [
        'https://result.doenets.lk/result/service/AlResult?index=7750000&nic=']
    custom_settings = {
        'ITEM_PIPELINES': {'examresults.pipelines.AdvancedLevelPipeline': 300, }
    }

    def parse(self, response):

        if response.json()['name'] is not None:
            items = AdvancedLevelItem()

            items['exam'] = response.json()['examination']
            items['year'] = response.json()['year']
            items['syllabus'] = response.json()['studentInfo'][2]['value']
            items['name'] = response.json()['name']
            items['indexNo'] = response.json()['indexNo']
            items['nic'] = response.json()['nic']
            items['drank'] = response.json()['districtRank']
            items['irank'] = response.json()['islandRank']
            items['zscore'] = response.json()['zScore']
            items['substream'] = response.json()['stream']
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

            yield items

        if AdvancedLevelSpider.number < 9999999:

            AdvancedLevelSpider.number += 1

            next_page = 'https://result.doenets.lk/result/service/AlResult?index=' + \
                str(AdvancedLevelSpider.number) + '&nic='
            yield response.follow(next_page, callback=self.parse)
