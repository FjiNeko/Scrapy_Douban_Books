from scrapy import cmdline
cmdline.execute('scrapy crawl books -o book.csv'.split())
