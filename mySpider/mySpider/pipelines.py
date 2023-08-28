# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from config import GiteeDownLoad
from git.repo import Repo
import os
import shutil
import stat
class MyspiderPipeline:
    # 构造方法
    def __init__(self):
        self.fp = None  # 定义一个文件描述符属性
        pass

    # 开始爬虫时，执行一次
    def open_spider(self, spider):
        print('爬虫开始')
        self.fp = open('./pinfo_c.json', 'w', encoding='utf-8')
        # self.fp = open('./pindex.txt', 'w', encoding='utf-8')
        # self.fp = open('./plist.txt', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        json_str = json.dumps(item, ensure_ascii=False)
        self.fp.write(json_str + '\n')
        # download_path = os.path.join('santa', 'NB')
        # self.fp.write(str(item['link']) + '\n')
        print("爬取中")
        return item

    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()
