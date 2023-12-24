import scrapy
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/top250?start=0"]

    def parse(self, response):
        # 爬取页面源代码
        book_list = response.xpath('//div[@class="pl2"]')
        readable_T = '[可试读]'
        readable_F = '[不可试读]'
        # 从源代码中爬取信息
        for book in book_list:
            book_item = BookItem()
            book_item['title'] = book.xpath('.//a/text()').get().strip()
            book_item['cover'] = book.xpath('//*[@class="nbg"]/img/@src').get()
            readable = book.xpath('./img/@title').get()
            if readable == '可试读':
                book_item['readable'] = readable_T
            else:
                book_item['readable'] = readable_F
            infos = book.xpath('./p[@class="pl"]/text()[1]').get()
            # book_item['author'] = info_list[0]
            print(infos)
            yield book_item

        # 提取下一页的链接
        # next_page = response.xpath('//span[@class="next"]/a/@href').get()
        # if next_page:
        #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)




