#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy

#tilte link date sort

#import win32api

#f=open("C:\Users\leeheekyo\Documents\python\crawl",'w')

#취업 : \ucde8\uc5c5
#인턴 : \uc778\ud134
#멘토 : \uba58\ud1a0

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    count = 0
    start_urls = [
        #"http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse"
        "http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=1&search=%EC%B7%A8%EC%97%85&column=title",
        "http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=2&search=%EC%B7%A8%EC%97%85&column=title",
        #"http://uwcms.pusan.ac.kr/user/indexSub.action?codyMenuSeq=21679&siteId=cse&dum=dum&boardId=10418&page=3&search=%EC%B7%A8%EC%97%85&column=title",

        #max 55!
    ]
    f= open("test.html","w")

    def parse(self, response):
        if( self.count==0 ) :
            self.f.write("<html>\n<body>\n<h1>WYW</h1>\n<div id=\"out0\" />\n")
            self.f.write("<script>\nvar text = \'[\'+\n")
        self.count += 1

        for sel in response.xpath('//*[@id="board-container"]/div[2]/form[1]/table/tbody'): # //ul/li
            i=0

            while(i<22):
                link_s="http://uwcms.pusan.ac.kr/user/"
                path='tr['+ str(i+1)+ ']/td[2]/strong/a/@href'
                link=str(sel.xpath('tr['+ str(i+1)+ ']/td[2]/strong/a/@href').extract())
                if(len(link)<3):
                    link=str(sel.xpath('tr['+ str(i+1)+ ']/td[2]/a/@href').extract())

                j=0
                while(link[j]!="\'"):
                    j+=1
                j+=1
                link=link[j:]
                while(link[j]!="\'"):
                    j+=1
                link=link[0:j]
                link_s+=link

                if(len(link)<4):
                    i+=1
                    continue

                path = 'tr['+str(i+1)+']/td[2]/strong/a'
                title=""
                title_s=str(sel.xpath(path).extract())
                if(len(title_s)<3):
                    path='tr['+ str(i+1)+ ']/td[2]/a'
                    title_s=str(sel.xpath(path).extract()).decode('utf-8')
                j=0
                while(title_s[j]!=">"):
                    j+=1
                j+=1
                sig_val =0;
                while(title_s[j]!="<" and j<len(title_s)-1 ):
                    if(title_s[j]==' '):
                        j+=1
                        continue
                    if(title_s[j]=="\\" and (title_s[j+1]=='n' or title_s[j+1]=='r' or title_s[j+1]=='t') ):
                        j+=2
                        continue
                    if(title_s[j]=='\\' and title_s[j+1]=='u' and title_s[j+2]=='c' and title_s[j+3]=='d' and title_s[j+4]=='e' and title_s[j+5]=='8' and title_s[j+6]=='\\' and title_s[j+7]=='u' and title_s[j+8]=='c' and title_s[j+9]=='5' and title_s[j+10]=='c' and title_s[j+11] == '5') :
                        sig_val=1
                        #print "취업".encode("utf-8") #\ucde8\uc5c5
                    title+=title_s[j]
                    #if((title_s[j]=='\\' and title_s[j+1]=='t') or (title_s[j]=='\\' and title_s[j+1]=='r')or(title_s[j]=='\\' and title_s[j+1]=='n')):
                    #    j+=2
                    #    continue
                    #if(title_s[j]=='\\' and title_s[j+1]=='u'):
                    #    j+=2
                    #    title+=title_s[j:j+4]
                    #    j+=4
                    #else:
                    #    title+=title_s[j]
                    j+=1


                path='tr['+ str(i+1)+ ']/td[4]'
                date_txt=str(sel.xpath(path).extract())

                j=0
                date_s=''
                while(j<len(date_txt) ):
                    if( (date_txt[j]>='0'and date_txt[j]<='9') or (date_txt[j]=='-') ):
                        date_s+= date_txt[j]
                    j+=1

#                print link_s , date_s, title.encode("utf-8")
#                if(sig_val==1): print("취업")
                i+=1

                self.f.write('\'{\"title\":\"')
                self.f.write(title)
                self.f.write('\", \"date\":\"')
                self.f.write(date_s)
                self.f.write('\", \"link\":\"')
                self.f.write(link_s)
                self.f.write('\", \"kind\":\"')
                if(sig_val==1): self.f.write("취업")
                self.f.write('\"},\'+\n')

        if(self.count==2):
            self.f.seek(self.f.tell()-5)
            self.f.write('\'+\n')
            self.f.write('\']\';\n')
            self.f.write('var obj=JSON.parse(text);\n')
            self.f.write('var out=\"<table>\";\nvar i;\n')
            self.f.write('for(i = 0; i < obj.length; i++) {\n')
            self.f.write('out+= \"<tr><td>\" + obj[i].title + \"</td><td>\" +')
            self.f.write('obj[i].date + \"</td><td>\" +')
            self.f.write('obj[i].link + \"</td><td>\" +')
            self.f.write('obj[i].kind + \"</td></tr>\";\n}\n')
            self.f.write('out+=\"</table>\";\n')
            self.f.write('document.getElementById(\"out0\").innerHTML = out;\n')
            self.f.write('</script>\n</body>\n</html>')
