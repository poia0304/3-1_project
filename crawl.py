#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy

#import win32api

#f=open("C:\Users\leeheekyo\Documents\python\crawl",'w')


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        #"http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse"
        "http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=1&search=%EC%B7%A8%EC%97%85&column=title"
    ]

    def parse(self, response):
        #print response.xpath('//*[@id="board-container"]/div[2]/form[1]/table/tbody/tr[1]/td[2]/strong/a/@href').extract()
        for sel in response.xpath('//*[@id="board-container"]/div[2]/form[1]/table/tbody'): # //ul/li
            #title = sel.xpath('a/text()').extract()
            #link = sel.xpath('a/@href').extract()
            #desc = sel.xpath('text()').extract()
            #print title, link, desc

            #test = sel.xpath('//td')#찾기
            #test = sel.xpath('//td/text()') #배제
            #//*[@id="board-container"]/div[2]/form[1]/table/tbody/tr[8]/td[2]/a

            test=sel.xpath('//tr/td[2]/strong/a/@href').extract()
            #print test
            test=sel.xpath('//tr/td[2]/a/@href').extract()
            #print test
            tt=str(test)
            ttt = tt.split()
            for tttt in ttt :
                i=0
                while(tttt[i]!="\'"):
                    i+=1
                i+=1
                start=i
                while(tttt[i]!="\'"):
                    i+=1
                end=i
                print tttt[start:end]
#            f.write(title , link, desc)

