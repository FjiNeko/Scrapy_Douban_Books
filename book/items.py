# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # 你可以在此处进行自定义，但是请遵守以下格式:
    # name = scrapy.Field()
    title = scrapy.Field() #获取标题
    cover = scrapy.Field() #获取封面图片 url
    readable = scrapy.Field() #定义是否“试读”
    author = scrapy.Field() #定义作者
    publisher = scrapy.Field() #定义出版社
    pubish_date = scrapy.Field() #定义出版日期
    price = scrapy.Field() #定义参考定价
    rating = scrapy.Field() #定义评分
    comment_count = scrapy.Field() #定义评价人数
