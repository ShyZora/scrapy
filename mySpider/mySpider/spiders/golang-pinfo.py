# import re
# from datetime import datetime
#
# from fossxkb.utils import AbstractPinfoSpider, GeneralPinfoItem
# from scrapy import Request
#
#
# class GolangPinfoSpider(AbstractPinfoSpider):
#     name = 'golang-pinfo'
#     custom_settings = {
#         # 'DOWNLOAD_DELAY': .025,
#         'CONCURRENT_REQUESTS_PER_DOMAIN': 10
#     }
#
#     def process_line(self, line, index):
#         if line.startswith('#') or not line.isascii():
#             return
#         # self.logger.debug(f'#{index}: {line}')
#         entity = GeneralPinfoItem()
#         entity['language'] = 'golang'
#         entity['_source'] = line
#         entity['name'] = line
#         entity['package_manager'] = 'golang'
#         entity['releases'] = []
#         entity['_extra'] = {}
#         url = f'https://pkg.go.dev/{line}'
#         yield Request(url, self.parse,
#                       cb_kwargs={'entity': entity})
#
#     def parse(self, response, **kwargs):
#         # self.logger.debug(f'Parsing {response.url}')
#         entity = kwargs['entity']
#         text = response.xpath('//a[@data-test-id="UnitHeader-license"]/text()').extract_first()
#         entity['license'] = text
#         unitmeta = response.xpath('//div[@class="UnitMeta"]')
#         project_url = unitmeta.css('div.UnitMeta-repo > a').xpath('@href').extract_first()
#         valid_gomod = unitmeta.css('ul.UnitMeta-details > li:first-child img').xpath('@alt').extract_first()
#         # self.logger.debug(f'valid_gomod={valid_gomod}')
#         entity['_extra'] = {'gomod': valid_gomod}
#         entity['project_url'] = project_url
#         status = response.status
#         versions_url = response.urljoin('?tab=versions')
#         yield Request(versions_url, self.parse_versions, cb_kwargs=kwargs)
#
#     def parse_versions(self, response, **kwargs):
#         entity = kwargs['entity']
#         entity['releases'] = []
#         for tag_elem in response.css('div.Version-tag'):
#             # version_link = tag_elem.xpath('a/@href').get()
#             version = tag_elem.xpath('a/text()').get()
#             version_url = tag_elem.xpath('a/@href').get()
#             release_date = None
#             next_two = tag_elem.xpath('following-sibling::*[2]')
#             class_name = next_two.xpath('@class').get()
#             date_str = None
#             # Examples
#             # https://pkg.go.dev/github.com/charmbracelet/bubbletea?tab=versions
#             if class_name == 'Version-commitTime':
#                 date_str = next_two.xpath('text()').get()
#             elif 'Version-details' in class_name:
#                 # Case of: <summary class="Version-summary"> May  5, 2023 </summary>
#                 date_str = next_two.xpath('summary/text()').get()
#             if date_str is not None:
#                 date_str = date_str.strip()
#                 if date_str != 'date unknown':
#                     try:
#                         release_date = datetime.strptime(date_str.strip(), '%b %d, %Y').strftime("%Y-%m-%d")
#                     except ValueError:
#                         self.logger.warn(f'无法解析时间 "{date_str}": {response.url}')
#             source_url = None
#             project_url = entity.get('project_url')
#             if project_url is not None and re.match('https://github\.com/.*', project_url):
#                 source_url = f'{project_url}/archive/refs/tags/{version}.zip'
#             entity['releases'].append({'version': version, 'release_date': release_date,
#                                        'source_url': source_url,
#                                        'version_url': response.urljoin(version_url)})
#             # self.logger.debug(f'version={version}, link={version_link}, sib={release_date}')
#
#         project_url = entity.get('project_url')
#         if project_url is not None and re.match('https://github\.com/.*', project_url):
#             yield Request(project_url.replace("https://github.com", "https://kgithub.com"), self.parse_github,
#                           # errback=self.parse_github_error,
#                           cb_kwargs=kwargs)
#         else:
#             self.process_stats()
#             yield entity
#
#     def parse_github(self, response, **kwargs):
#         entity = kwargs['entity']
#         right_panel = response.css('.Layout-sidebar .BorderGrid-row > .BorderGrid-cell')
#         for div in right_panel:
#             title = div.css('h2::text').get()
#             if title is not None:
#                 title = title.strip()
#
#             # self.logger.debug(f'Found sidebar block: {title}')
#             if title == "About":
#                 # text = div.css('p::text').get()
#                 # The <p> may contains other element like <a>, e.g. https://github.com/p7zip-project/p7zip
#                 # https://stackoverflow.com/questions/51742945/extract-all-elements-from-within-p-tag-scrapy
#                 about = ' '.join([el.strip() for el in div.xpath('p//text()').extract()]).strip()
#                 entity.set_summary(about)
#                 break
#         self.process_stats()
#         yield entity
#
#     def parse_github_error(self, failure):
#         args = failure.request.cb_kwargs
#         entity = args['entity']
#         self.process_stats()
#         yield entity
