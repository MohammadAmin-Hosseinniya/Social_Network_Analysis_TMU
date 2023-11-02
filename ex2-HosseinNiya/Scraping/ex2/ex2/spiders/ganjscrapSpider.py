import scrapy
import requests
import json

from ..items import ex2Item

class GanjscrapspiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["ganj.irandoc.ac.ir"]
    start_urls = ['https://ganj.irandoc.ac.ir/api/v1/search/main?basicscope=1&keywords=%D8%A7%D9%85%DB%8C%D8%B1+%D8%A7%D9%84%D8%A8%D8%AF%D9%88%DB%8C&page=1']

    url_format = 'https://ganj.irandoc.ac.ir/api/v1/search/main?basicscope=1&keywords=%D8%A7%D9%85%DB%8C%D8%B1+%D8%A7%D9%84%D8%A8%D8%AF%D9%88%DB%8C&page={page_number}'
    tags_url_format = "https://ganj.irandoc.ac.ir/api/v1/articles/{uuid}/show_tags"
      
    def parse(self, response):
        if "page=" not in response.url:
            page = 1
        else:
            page = int(response.url.split("page=")[-1])

        items = ex2Item()
                
        raw = json.loads(response.body)
        data = raw['results']
        number_of_pages = raw['total_pages']
        
        for i in data:
            items['title'] = i['title']
            if i['keywords_status']:
                doc_id = i['uuid']
                tags_url = self.tags_url_format.format(uuid = doc_id)
                r = requests.get(tags_url)
                if r.status_code == 200:
                    tags = json.loads(r.content)
                    tag = []
                    for t in tags['tags']:
                        tag.append(t['title_fa']) 
                    items['tags'] = tag
            
            yield items
        
        if page <= number_of_pages:
            yield scrapy.Request(self.url_format.format(page_number = page + 1), callback=self.parse)
            
            
