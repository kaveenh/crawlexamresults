from scrapy.crawler import CrawlerProcess
import scrapy
from scrapy.http import FormRequest
from ..items import ScholarshipItem
from scrapy.utils.response import open_in_browser
import json


class ScholarshipSpider(scrapy.Spider):
    name = 'scholarship1'
    number = 1000001
    start_urls = ['https://result.doenets.lk/result/service/GvResult/1000000']
    custom_settings = {
        'ITEM_PIPELINES': {'examresults.pipelines.ScholarshipPipeline': 300, }
    }

    # def __init__(self, task):
    #     scrapy.Spider.__init__(self)
    #     self.task = task

    # def start_requests(self):
    #     yield scrapy.Request(url=self.task['start_urls'], callback=self.parse, meta=self.task)

    def parse(self, response):

        if response.json()['name'] is not None:
            items = ScholarshipItem()

            items['exam'] = response.json()['examination']
            items['year'] = response.json()['year']
            items['indexNo'] = response.json()['indexNo']
            items['name'] = response.json()['name']
            items['marks'] = response.json()['marks']

            yield items

        if ScholarshipSpider.number < 3250000:

            ScholarshipSpider.number += 1

            next_page = 'https://result.doenets.lk/result/service/GvResult/' + \
                str(ScholarshipSpider.number) + '/'
            yield response.follow(next_page, callback=self.parse)

        # sessionid = response.css(
        #     'form input[name="examSessionId"]::attr(value)').extract_first()
        # year = response.css(
        #     'form input[name="year"]::attr(value)').extract_first()
        # typeTitle = response.css(
        #     'form input[name="typeTitle"]::attr(value)').extract_first()
        # isAddIndexNeeded = response.css(
        #     'form input[name="isAddIndexNeeded"]::attr(value)').extract_first()
        # additionalFieldName = response.css(
        #     'form input[name="additionalFieldName"]::attr(value)').extract_first()
        # comment = response.css(
        #     'form input[name="comment"]::attr(value)').extract_first()

        # return FormRequest.from_response(response, formdata={

        #     'examSessionId': sessionid,
        #     'year': '2020',
        #     'typeTitle': 'Grade 5 Scholarship Examination',
        #     'isAddIndexNeeded': 'N',
        #     'additionalFieldName': '',
        #     'comment': '',
        #     'indexNumber': '5235960'
        # }, callback=self.start_scrapping)

    # def start_scrapping(self, response):
    #     # items = ExamresultsItem()
    #     open_in_browser(response)
