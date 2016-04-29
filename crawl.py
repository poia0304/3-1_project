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
        "http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=1&search=%EC%B7%A8%EC%97%85&column=title",
        "http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=2&search=%EC%B7%A8%EC%97%85&column=title",
        "http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=3&search=%EC%B7%A8%EC%97%85&column=title"
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

            i=0
            #//*[@id="board-container"]/div[2]/form[1]/table/tbody/tr[1]/td[2]/strong/a
            #//*[@id="board-container"]/div[2]/form[1]/table/tbody/tr[2]/td[2]/strong/a
            #print sel.xpath('tr[2]/td[2]/strong/a/@href').extract()
            while(i<22):
                path='tr['+ str(i+1)+ ']/td[2]/strong/a/@href'
                test=str(sel.xpath('tr['+ str(i+1)+ ']/td[2]/strong/a/@href').extract())
                if(len(test)<3):
                    test=str(sel.xpath('tr['+ str(i+1)+ ']/td[2]/a/@href').extract())

                j=0
                while(test[j]!="\'"):
                    j+=1
                j+=1
                test=test[j:]
                while(test[j]!="\'"):
                    j+=1
                test=test[0:j]

                path='tr['+ str(i+1)+ ']/td[4]'
                test2_txt=str(sel.xpath(path).extract())

                j=0
                test2=''
                while(j<len(test2_txt) ):
                    if( (test2_txt[j]>='0'and test2_txt[j]<='9') or (test2_txt[j]=='-') ):
                        test2+= test2_txt[j]
                    j+=1

                if(len(test)>3):
                    print test , test2
                i+=1


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
                #print tttt[start:end]

            test = sel.xpath('//tr/td[4]').extract()
            tt=str(test)
            ttt = tt.split('u')
            for tttt in ttt :
                i=0
                printlist=''
                while(i<len(tttt) ):
                    if( (tttt[i]>='0'and tttt[i]<='9') or (tttt[i]=='-') ):
                        printlist+= tttt[i]
                    i+=1
                end=i
                if(len(printlist)>1 ):
                    if(printlist[0] == '2' and printlist[1]=='0') :
                        printlist #print printlist

#            f.write(title , link, desc)

