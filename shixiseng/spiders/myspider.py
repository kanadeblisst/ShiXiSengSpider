import scrapy
from shixiseng.items import MyItem
import base64
import re
from  fontTools.ttLib  import  TTFont


class MySpider(scrapy.Spider):
    name = 'shixiseng'

    start_urls = ['https://www.shixiseng.com/']
    allowed_domains = ['shixiseng.com']
    n = 1

    def decrypt(self, b64text):
        text = base64.b64decode(b64text)
        with open('temp.ttf', 'wb') as f:
            f.write(text)
        font = TTFont('temp.ttf')
        font.saveXML('temp.xml')
        words = '  0123456789一师X会四计财场DHLPT聘招工d周l端p年hx设程二五天tCG前KO网SWcgkosw广市月个BF告NRVZ作bfjnrvz三互生人政AJEI件M行QUYaeim软qu银y联'
        with open('temp.xml') as f:
            xml = f.read()
        temp1 = re.findall(r'<GlyphID id="(\d+)" name="(.*?)"/>', xml)
        temp2 = list(set(re.findall(r'<map code="(.*?)" name="(.*?)"/>', xml)))
        d2 = {x[1]: x[0] for x in temp2}
        wordtab = {chr(int(d2[x[1]], 16)): words[int(x[0])] for x in temp1 if not (x[0] == '0' or x[0] == '1')}
        self.tab = str.maketrans(wordtab)

    def parse(self, response):
        intern = response.css('.intern-type .type-item')
        for i in intern:
            #job_type = i.css('.type-list::attr(data-type)').get()
            for a in  i.css('.type-list div a[data-sname="43"]'):
                sub_type = a.css('a::text').get()
                yield response.follow(a, callback=self.parse_follow, meta={'sub_type':sub_type})


    def parse_follow(self, response):
        job_type = response.meta['sub_type']
        job_type = job_type.replace('/', '-')
        if self.n:
            b64text = re.search(r'base64,(.*?)"', response.text).group(1)
            self.decrypt(b64text)
            self.n = 0
        position_list = response.css('.position-list .position-item.clearfix.font')
        for position in position_list:
            job_name = position.css('.position-name::text').get()
            url = position.css('.position-name::attr(href)').get()
            salary = position.css('.position-salary::text').get()
            place = position.css('.info2.clearfix span:first-of-type::text').get()
            work_day = position.css('.info2.clearfix span:nth-child(2)::text').get()
            least_month = position.css('.info2.clearfix span:last-of-type::text').get()
            company = position.css('.company-name::text').get()
            category = position.css('.company-more-info.clearfix span:first-of-type::text').get()
            scale = position.css('.company-more-info.clearfix span:last-of-type::text').get().replace('/','')


            item = MyItem()
            item['job_name'] = job_name.translate(self.tab)
            item['_id'] = 'https://www.shixiseng' + url
            item['salary'] = salary.translate(self.tab)
            item['place'] = place.translate(self.tab)
            item['work_day'] = work_day.translate(self.tab)
            item['least_month'] = least_month.translate(self.tab)
            item['company'] = company.translate(self.tab)
            item['category'] = category.translate(self.tab) if category else ''
            item['scale'] = scale.translate(self.tab)
            item['mongo_set'] = job_type.translate(self.tab)

            yield item

        next_url = response.xpath('//div[@id="pagebar"]//li/a[text()="下一页"]/@href').get()
        if next_url:
            yield response.follow(next_url, callback=self.parse_follow, meta={'sub_type':job_type})



