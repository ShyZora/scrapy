import scrapy


class SpideSpider(scrapy.Spider):
    name = "spide"
    allowed_domains = "gitee.com"
    start_urls = ["https://gitee.com/fssssss/KuiperInferGitee"]

    def start_requests(self):

        # 指定你的cookies
        headers = {
            "cookie": "oschina_new_user=false; remote_way=http; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; slide_id=10; Hm_lvt_dbba4dc235af9a121ecb9ae949529239=1689319889,1689559065; user_locale=zh-CN; Hm_lvt_f25cb1a7bcd4301fa646f5a3d00bb96e=1690439165; Hm_lvt_508c175c9048c8cd35624a040399385b=1690798424; Serve_State=true; yp_riddler_id=a94a2184-960c-4b81-8f74-8a0589d8e499; tz=Asia%2FShanghai; Hm_lvt_24f17767262929947cc3631f99bfd274=1691030287,1691570412,1691631419,1691717257; BEC=1f1759df3ccd099821dcf0da6feb0357; user_return_to_0=%2Ffssssss%2FKuiperInferGitee%2Ftags; gitee_user=true; Hm_lvt_de4da04394d5af6213209e6ff7eeaed3=1691718966; Hm_lpvt_de4da04394d5af6213209e6ff7eeaed3=1691719029; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2210171285%22%2C%22first_id%22%3A%22189dea85607184f-01f8d1936b62f55-7c546c76-2073600-189dea856081df2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_utm_source%22%3A%22gitee_search%22%7D%2C%22%24device_id%22%3A%221891fd616d014ee-08b437e7d6fbdb-7e56547f-2073600-1891fd616d11ee6%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5MjlkMDYwODExOGUtMDNhYWMxMjQyYjhiNjljLTdlNTY1NDdmLTIwNzM2MDAtMTg5MjlkMDYwODJlM2UiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMDE3MTI4NSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2210171285%22%7D%7D; Hm_lvt_9e50a6aa51706b34aa4cdf1f17bce240=1691719850; Hm_lpvt_9e50a6aa51706b34aa4cdf1f17bce240=1691719918; Hm_lpvt_24f17767262929947cc3631f99bfd274=1691720148; gitee-session-n=bjRhb3A3SjNwUTFCbWxkZVVTUWN2MStya1B0S2IxclRDb09BNEZrTjNrWkdpQmN1Mm5UZVBNdGZRYjdVSFhmZHBNNlpCQWtZUzlwQUJRT0N5QjNLY2FBd0ZlaWJEZ1NUTUp5eDRDQ3dxOWFjNjBNVnYvcjNuOVRlemRLV0pnb2RxN1VpbmphN08vTFV0aUYveFdwaDRrcDREL2VvR095T1pPOElRdVQrdWxJTVlTaVE1ckNYTXd0OS9qSnpNeHZ4YjRPOHkwOUxsdWdEQkk4Uk13aXBYNC9nUUNCSk41M0VRRVg0RXFVdGlrRks1QXFrbW83WDMyT3MwcGJjTVVuYjcvUmlWWDFJNDNRM2pZOVBiVnI0VERqZjJvTkV4ZlkvYlZTUmdaMml6VWt6QUF3VEV2TVVvWHBibzVaVk1PQnVSSXIxK0ptL0NMRUtNK3cwNW1EZmgvME5Kb3YzWHU1OGprK0tJeEpmS1ZxVDFGU2ZaQU14OUk0M0VibHJsMExGWTNQRFl4aDM0YUo5MG9Pcm8xMFk0bGdVaFVzUjllTHMwWFVKeTZNTlZSZEFmcHBhdE5vVFhUV0h3aFBMZXV2MVlsck9MeENucWJWVk5ITERzTDhiRG12R01ZaVo5dWgyZ0hVYlZyN05WZktqU1FhemI2VzhBNmx1bUQ0aHl3MzJKanlSWlNaUFhRd0hlaG1RNlhGVmg2ZGRWSzZXZU45M0Y5ckoxMmkvemh4azFTR1Uvc1Z2N0lqSklnZ0JaZkExbUdOOE5IcVdybkZwajRqb0NVUXR3WXNxWnNFMTlhMktTT1VyVDBrUjR3SlA3OXFOUVlhb2craEtncG9GcTVlci0teElGa2x5akVUeWs3d25FdUwxRFpKZz09--030a271f24691220bb5f2ee22fe0218b4b3ff22d"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
        print(response.url)
        print(response.xpath(
            '/html/body/div[@class="site-content"]//div[@class="git-project-download-panel for-project ui bottom right popup"]//a[@class="ui fluid download link button"]').get())
        print("dasdsadasasdasd")
        # tag list
        # tag_list = response.xpath('//div[@class="tag-list"]')
        # if tag_list is not None:
        #     path = tag_list.xpath('./div[@class="item tag-item"]')
        #     # print(path.get())
        #     for i in path:
        #         # print(i.get())
        #         # walk = i.xpath('./div[@class="tag-item-action tag-last-commit"]/div[@class="tag-item-action-row"]').get())
        #         # date = i.xpath('./div[@class="tag-item-action tag-last-commit"]/div[2]/text()')
        #         # print(date.get())
        #
        #         # walk = i.xpath('.//a')
        #         # # print(walk.get())
        #         # print(walk.xpath('./@title').get())
        #         # print(walk.xpath('./@href').get())

    def parse_tags(self, response):
        print(response.url, end='')
        print("dasdsadasasdasd")

    # def parse(self, response):
    #     elements = response.xpath('//div[@class="ui relaxed divided items explore-repo__list"]//div[@class="item"]')
    #     for element in elements:
    #         link = self.allowed_domains + element.xpath('.//h3/a/@href').get()
    #         print(link)
    #         desc = element.xpath('.//div[@class="project-desc"]/text()').get()
    #
    #     # 注意：根据多个属性值进行xpath的时候，用and来连接。
    #         next_href__get = response.xpath(
    #             '//div[@class="ui tiny pagination menu"]//a[@class="icon item" and @rel="next"]/@href'
    #         ).get()
    #     #
    #     if next_href__get is not None:
    #         print("https://gitee.com" + next_href__get)
    #         # 如果存在下一页则继续请求
    #         print("继续请求")
    #         yield scrapy.Request("https://gitee.com" + next_href__get, callback=self.parse, dont_filter=True)

    #
    # start = response.xpath('//a[@class="ui button action-social-count "]/text()')
    # fork = response.xpath('//a[@class="ui button action-social-count disabled-style"]/text()')
    # licence = response.xpath('//div[@class="intro-list"]/div[@class="item"]/a[@id="license-popup"]/text()')
    # summary = response.xpath('//div[@class="content"]/span[@class="git-project-desc-text"]/text()')
    # master_zip = response.xpath('//div[@class="site-content"]/div[@class="ui container"]//div[@class="git-project-content"]//div[@class="git-project-right-actions pull-right"]')
    # license_url = response.xpath('//div[@class="intro-list"]//a[@id="license-popup"]/@href')
    # print(response.url)
    # yield scrapy.Request(response.url, callback=self.parse_tags, dont_filter=True)

    # elements = response.xpath('//div[@class="ui popup summary-languages-popup"]//div[@class="row"]')
    # for i in elements:
    # 语言类型
    # print(i.xpath('./div[@class="lang"]/a/text()').get())
    # print(i.xpath('./a/text()').get())
    # pass
