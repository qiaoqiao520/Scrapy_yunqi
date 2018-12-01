# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import xlwt


class YunqiprojectPipeline(object):
    def process_item(self, item, spider):
        return item


class SqlitePipeline(object):

    def open_spider(self, spider):
        """程序开始运行时调用"""
        self.create_table()

    def create_table(self):
        self.connect_sql()
        sql = 'CREATE TABLE IF NOT EXISTS yunqi (id INTEGER PRIMARY KEY , novel_name CHAR , introduce CHAR , img_src CHAR , all_click CHAR , all_popular CHAR , all_recommend CHAR , month_click CHAR , month_popular CHAR , month_recommend CHAR , week_click CHAR , week_popular CHAR , week_recommend CHAR , all_word CHAR , comment CHAR , state CHAR )'
        self.cursor.execute(sql)
        self.close_sql()

    def connect_sql(self):
        self.coon = sqlite3.connect('yunqi.db')
        self.cursor = self.coon.cursor()

    def close_sql(self):
        self.coon.commit()
        self.cursor.close()
        self.coon.close()

    def process_item(self, item, spider):
        self.connect_sql()
        sql = 'INSERT INTO yunqi (novel_name, introduce, img_src, all_click, all_popular, all_recommend, month_click, month_popular, month_recommend, week_click, week_popular, week_recommend, all_word, comment, state) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item['novel_name'], item['introduce'], item['src'], item['all_click'], item['all_popular'], item['all_recommend'], item['month_click'], item['month_popular'], item['month_recommend'], item['week_click'], item['week_popular'], item['week_recommend'], item['all_word'], item['comment'], item['state'])
        self.cursor.execute(sql)
        self.close_sql()
        return item


class ExcelPipeline(object):
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workbook.add_sheet('yunqi')
        self.count = 0
        self.create_excel()

    def create_excel(self):
        self.sheet.write(0, 0, '小说名称')
        self.sheet.write(0, 1, '小说简介')
        self.sheet.write(0, 2, '封面图地址')
        self.sheet.write(0, 3, '总点击')
        self.sheet.write(0, 4, '总人气')
        self.sheet.write(0, 5, '总推荐')
        self.sheet.write(0, 6, '月点击')
        self.sheet.write(0, 7, '月人气')
        self.sheet.write(0, 8, '月推荐')
        self.sheet.write(0, 9, '周点击')
        self.sheet.write(0, 10, '周人气')
        self.sheet.write(0, 11, '周推荐')
        self.sheet.write(0, 12, '总字数')
        self.sheet.write(0, 13, '评论数')
        self.sheet.write(0, 14, '连载状态')

    def process_item(self, item, spider):
        self.count += 1
        print('正在保存第{}本小说:{}'.format(self.count, item['novel_name']))
        self.sheet.write(self.count, 0, item['novel_name'])
        self.sheet.write(self.count, 1, item['introduce'])
        self.sheet.write(self.count, 2, item['src'])
        self.sheet.write(self.count, 3, item['all_click'])
        self.sheet.write(self.count, 4, item['all_popular'])
        self.sheet.write(self.count, 5, item['all_recommend'])
        self.sheet.write(self.count, 6, item['month_click'])
        self.sheet.write(self.count, 7, item['month_popular'])
        self.sheet.write(self.count, 8, item['month_recommend'])
        self.sheet.write(self.count, 9, item['week_click'])
        self.sheet.write(self.count, 10, item['week_popular'])
        self.sheet.write(self.count, 11, item['week_recommend'])
        self.sheet.write(self.count, 12, item['all_word'])
        self.sheet.write(self.count, 13, item['comment'])
        self.sheet.write(self.count, 14, item['state'])
        self.workbook.save('yunqi.xls')
        return item

    def close_spider(self, spider):
        self.workbook.save('yunqi.xls')