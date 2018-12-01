# -*- coding: utf-8 -*-
import scrapy
from ..items import ImgItem


class YunqiSpider(scrapy.Spider):
    name = 'yunqi'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n10p1']

    def parse(self, response):
        """解析一级页面"""
        urls = response.xpath('//div[@class="book_info"]/h3/a/@href').extract()
        for url in urls:
            # print(url)
            yield scrapy.Request(
                url=url,
                callback=self.parse_detail
            )

        # 找下一页链接
        page_next = response.xpath('//div[@class="page_wrap"]/div[@id="pageHtml2"]/a/span[contains(@class, "page-next")]').extract_first()
        # print(page_next)
        if page_next:
            url = response.xpath('//div[@class="page_wrap"]/div[@id="pageHtml2"]/a[last()]/@href').extract_first()
            # print(url)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )
        else:
            print('没有下一页了！！！')

    def parse_detail(self, response):
        """解析详情页面"""
        #小说名
        novel_name = response.xpath('//strong/a/text()').extract_first()
        # 简介
        introduce = response.xpath('//div[@class="info"]/p//text()').extract_first()
        # 封面图下载地址
        img = response.xpath('//a[@class="bookcover"]/img/@src').extract_first()
        img_src = 'http:' + img
        # 小说信息
        # 总点击
        all_click = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[2]/td[1]/text()').extract_first().split('：')[-1]
        # 总人气
        all_popular = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[2]/td[2]/text()').extract_first().split('：')[-1]
        # 总推荐
        all_recommend = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[2]/td[3]/text()').extract_first().split('：')[-1]
        # 月点击
        month_click = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[3]/td[1]/text()').extract_first().split('：')[-1]
        # 月人气
        month_popular = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[3]/td[2]/text()').extract_first().split('：')[-1]
        # 月推荐
        month_recommend = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[3]/td[3]/text()').extract_first().split('：')[-1]
        # 周点击
        week_click = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[4]/td[1]/text()').extract_first().split('：')[-1]
        # 周人气
        week_popular = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[4]/td[2]/text()').extract_first().split('：')[-1]
        # 周推荐
        week_recommend = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[4]/td[3]/text()').extract_first().split('：')[-1]
        # 总字数
        all_word = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[5]/td[1]/text()').extract_first().split('：')[-1]
        # 评论数
        comment = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[5]/td[2]/span/text()').extract_first()
        # 连载状态
        state = response.xpath('//div[@class="middle"]/div[@id="novelInfo"]/table/tr[5]/td[3]/span/text()').extract_first()
        # print(novel_name, introduce, img_src, all_click, all_popular, all_recommend, month_click, month_popular, month_recommend, week_click, week_popular, week_recommend, all_word, comment, state)

        # 创建item对象
        item = ImgItem()
        item['novel_name'] = novel_name
        item['src'] = [img_src]
        item['introduce'] = introduce
        item['all_click'] = all_click
        item['all_popular'] = all_popular
        item['all_recommend'] = all_recommend
        item['month_click'] = month_click
        item['month_popular'] = month_popular
        item['month_recommend'] = month_recommend
        item['week_click'] = week_click
        item['week_popular'] = week_popular
        item['week_recommend'] = week_recommend
        item['all_word'] = all_word
        item['comment'] = comment
        item['state'] = state

        yield item



