# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScholarshipItem(scrapy.Item):

    # scholarship student item
    exam = scrapy.Field()
    year = scrapy.Field()
    indexNo = scrapy.Field()
    name = scrapy.Field()
    marks = scrapy.Field()
    pass


class AdvancedLevelItem(scrapy.Item):

    # advanced level student item
    exam = scrapy.Field()
    year = scrapy.Field()
    syllabus = scrapy.Field()
    name = scrapy.Field()
    indexNo = scrapy.Field()
    nic = scrapy.Field()
    drank = scrapy.Field()
    irank = scrapy.Field()
    zscore = scrapy.Field()
    substream = scrapy.Field()
    sub1 = scrapy.Field()
    sub1grade = scrapy.Field()
    sub2 = scrapy.Field()
    sub2grade = scrapy.Field()
    sub3 = scrapy.Field()
    sub3grade = scrapy.Field()
    sub4 = scrapy.Field()
    sub4grade = scrapy.Field()
    sub5 = scrapy.Field()
    sub5grade = scrapy.Field()

    pass


class OrdinaryLevelItem(scrapy.Item):

    # ordinary level student item
    exam = scrapy.Field()
    year = scrapy.Field()
    name = scrapy.Field()
    indexNo = scrapy.Field()
    nic = scrapy.Field()
    sub1 = scrapy.Field()
    sub1grade = scrapy.Field()
    sub2 = scrapy.Field()
    sub2grade = scrapy.Field()
    sub3 = scrapy.Field()
    sub3grade = scrapy.Field()
    sub4 = scrapy.Field()
    sub4grade = scrapy.Field()
    sub5 = scrapy.Field()
    sub5grade = scrapy.Field()
    sub6 = scrapy.Field()
    sub6grade = scrapy.Field()
    sub7 = scrapy.Field()
    sub7grade = scrapy.Field()
    sub8 = scrapy.Field()
    sub8grade = scrapy.Field()
    sub9 = scrapy.Field()
    sub9grade = scrapy.Field()

    pass
