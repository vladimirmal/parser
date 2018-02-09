# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from questions.models import Questions
from scrapy_project.check_seo import Check


class ScrapyProjectPipeline(object):
    result = {}
    resultkey = {}
    resultdesc = {}
    resultlink = []
    resulth1 = {}
    resulttext = {}
    resultgoogl={}
    resultyandex={}
    def process_item(self, item, spider):
        #try:
         #   question = Questions.objects.get(identifier=item["identifier"])
          #  print ("Question already exist")
           # return item
        #except Questions.DoesNotExist:
         #   pass
        #         item =item['url']
       # question.save()
        if item['title']:
            self.result[item['link']] = item['title']
        self.resultkey[item['link']] = item['keyword']
        if item['description']:
            self.resultdesc[item['link']] = item['description']
        self.resultlink.append(item["link"])
        self.resulth1[item['link']] = item['h1']
        self.resulttext[item['link']] = item['text']
        self.resultgoogl[item['link']] = item['googl_anal']
        self.resultyandex[item['link']] = item['yandex_metrick']
        return item
