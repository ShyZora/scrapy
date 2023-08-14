import time

import scrapy

from mySpider.items import GiteePInfo, GiteePIndex


class GiteePinfoSpider(scrapy.Spider):
    name = "gitee-pinfo"
    allowed_domains = "https://gitee.com"
    start_urls = [line.strip() for line in open('./pindex.txt', 'r')]
    # start_urls = ["https://gitee.com/oscc-project/iEDA"]

    def parse(self, response):
        print(response.url)
        print(self.start_urls.find(response.url))
        _extra = {}
        langs = []
        elements = response.xpath('//div[@class="ui popup summary-languages-popup"]//div[@class="row"]')
        stars = response.xpath('//a[@class="ui button action-social-count "]/text()').get().strip()
        forks = response.xpath('//a[@class="ui button action-social-count disabled-style"]/text()').get().strip()
        license_url = response.xpath('//div[@class="intro-list"]//a[@id="license-popup"]/@href').get()
        summary = response.xpath('//div[@class="content"]/span[@class="git-project-desc-text"]/text()').get()
        licence = response.xpath('//div[@class="intro-list"]/div[@class="item"]/a[@id="license-popup"]/text()').get()
        main_branch = response.xpath('//div[@class="item git-project-branch-item"]//div[@class="default text"]/text()').get().strip()
        main_language = response.xpath('//div[@class="four wide column"]//span[@class="summary-languages"]/text()').get().strip()
        if elements is None:
            langs.append({'language': main_language, 'percent': 100})
        else:
            for element in elements:
                language = element.xpath('./div[@class="lang"]/a/text()').get()
                percent = float(element.xpath('./a/text()').get().replace('%', ''))
                langs.append({'language': language, 'percent': percent})
        item = GiteePInfo()
        _extra['langs'] = langs
        _extra['stars'] = stars
        _extra['forks'] = forks
        _extra['master_zip'] = response.url + '/repository/blazearchive/' + main_branch + '.zip'
        if license_url is None:
            _extra['license_url'] = self.allowed_domains
        else:
            _extra['license_url'] = self.allowed_domains + license_url
        item['_extra'] = _extra
        item['_source'] = response.url
        item['package_manager'] = 'gitee'
        item['project_url'] = response.url
        item['name'] = response.url[len(self.allowed_domains)+1:].replace('/', ':')
        if licence is None:
            item['license'] = ""
        else:
            item['license'] = licence
        item['summary'] = summary
        item['language'] = main_language
        time.sleep(0.1)
        yield scrapy.Request(response.url + '/tags',
                             callback=self.parse_tags,
                             cb_kwargs=item,
                             dont_filter=True)

    def parse_tags(self, response, **kwargs):
        kwargs['releases'] = []
        tag_list = response.xpath('//div[@class="tag-list"]')
        if tag_list is not None:
            for element in tag_list.xpath('./div[@class="item tag-item"]'):
                release = {}
                _tag = element.xpath('./div[@class="tag-item-action tag-name"]/a/@title').get().strip()
                release_date = element.xpath('./div[@class="tag-item-action tag-last-commit"]/div[2]/text()').get().strip().split(' ')[0]
                release['_tag'] = _tag
                release['release_date'] = release_date
                release['version'] = _tag
                release['_warn'] = 'BadVersion'
                release['source_url'] = ''
                kwargs['releases'].append(release)
        yield kwargs
