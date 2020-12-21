# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScholarshipPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):  # create sql database for scholarship students
        self.conn = sqlite3.connect("grade5.db")
        self.curr = self.conn.cursor()

    def create_table(self):  # create sql table to store scholarship results
        self.curr.execute("""drop table if exists grade5_tb""")
        self.curr.execute("""create table grade5_tb(
                exam text,
                year text,
                indexNo text,
                name text,
                marks text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):  # storing the scraped data of the scholarship students
        self.curr.execute("""insert into grade5_tb values(?,?,?,?,?)""", (
            item['exam'],
            item['year'],
            item['indexNo'],
            item['name'],
            item['marks']
        ))
        self.conn.commit()


class AdvancedLevelPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):  # create sql database for advanced level students
        self.conn = sqlite3.connect("advancedlevel.db")
        self.curr = self.conn.cursor()

    def create_table(self):  # create sql table to store advanced level results
        self.curr.execute("""drop table if exists advancedlevel_tb""")
        self.curr.execute("""create table advancedlevel_tb(
                exam text,
                year text,
                syllabus text,
                name text,
                indexNo text,
                nic text,
                drank text,
                irank text,
                zscore text,
                substream text,
                sub1 text,
                sub1grade text,
                sub2 text,
                sub2grade text,
                sub3 text,
                sub3grade text,
                sub4 text,
                sub4grade text,
                sub5 text,
                sub5grade text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):  # storing the scraped data of the advanced level students
        self.curr.execute("""insert into advancedlevel_tb values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            item['exam'],
            item['year'],
            item['syllabus'],
            item['name'],
            item['indexNo'],
            item['nic'],
            item['drank'],
            item['irank'],
            item['zscore'],
            item['substream'],
            item['sub1'],
            item['sub1grade'],
            item['sub2'],
            item['sub2grade'],
            item['sub3'],
            item['sub3grade'],
            item['sub4'],
            item['sub4grade'],
            item['sub5'],
            item['sub5grade']
        ))
        self.conn.commit()


class OrdinaryLevelPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):  # create sql database for ordinary level students
        self.conn = sqlite3.connect("ordinarylevel.db")
        self.curr = self.conn.cursor()

    def create_table(self):  # create sql table to store ordinary level results
        self.curr.execute("""drop table if exists ordinarylevel_tb""")
        self.curr.execute("""create table ordinarylevel_tb(
                exam text,
                year text,
                name text,
                indexNo text,
                nic text,
                sub1 text,
                sub1grade text,
                sub2 text,
                sub2grade text,
                sub3 text,
                sub3grade text,
                sub4 text,
                sub4grade text,
                sub5 text,
                sub5grade text,
                sub6 text,
                sub6grade text,
                sub7 text,
                sub7grade text,
                sub8 text,
                sub8grade text,
                sub9 text,
                sub9grade text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):  # storing the scraped data of the ordinary level students
        self.curr.execute("""insert into ordinarylevel_tb values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            item['exam'],
            item['year'],
            item['name'],
            item['indexNo'],
            item['nic'],
            item['sub1'],
            item['sub1grade'],
            item['sub2'],
            item['sub2grade'],
            item['sub3'],
            item['sub3grade'],
            item['sub4'],
            item['sub4grade'],
            item['sub5'],
            item['sub5grade'],
            item['sub6'],
            item['sub6grade'],
            item['sub7'],
            item['sub7grade'],
            item['sub8'],
            item['sub8grade'],
            item['sub9'],
            item['sub9grade']
        ))
        self.conn.commit()
