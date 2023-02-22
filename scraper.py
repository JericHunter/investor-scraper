import scrapy
import tldextract
from collections import defaultdict
import json


class AmplifyPortfolioSpider(scrapy.Spider):
    name = "amplify_portfolio"
    start_urls = ["https://www.amplifypartners.com/portfolio"]

    def parse(self, response, **kwargs):
        link_dict = defaultdict(list)
        for company_tag in response.css('.website__link-wr'):
            company_links = company_tag.css('a')
            if company_links:
                hrefs = company_links.attrib['href']
                domains = hrefs.split(',')[0][0:-1]
                company_name = tldextract.extract(domains).domain.capitalize()
                link_dict[company_name].append(domains)
        return {response.url: link_dict}

