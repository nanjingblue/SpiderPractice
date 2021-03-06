 # coding:utf-8
# import re
# from urllib.parse import urljoin
# from bs4 import BeautifulSoup

# class HtmlParser(object):
#     def parser(self, page_url, html_cont):
#         if page_url is None or html_cont is None:
#             return
#         soup = BeautifulSoup(html_cont, 'html.parser')
#         new_urls = self.get_new_urls(page_url, soup)
#         new_data = self.get_new_data(page_url, soup)
#         return new_urls, new_data

#     def get_new_urls(self, page_url, soup):
#         new_urls = set()
#         links = soup.find_all('a', href=re.compile(r'/\/item\/.+\/\d+\b'))
#         for link in links:
#             new_url = link['href']
#             # 拼接
#             new_full_url = urljoin(page_url, new_url)
#             new_urls.add(new_full_url)
#             return new_urls
#     def get_new_data(self, page_url, soup):
#         data = {}
#         data['url'] = page_url
#         title = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
#         data['title'] = title.get_text()
#         summary = soup.find('div', class_='lemma-summary')
#         data['summary'] = summary.get_text()
#         return data

#coding:utf-8
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup:soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标签
        links = soup.find_all('a',href=re.compile(r'/item/'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urljoin(page_url,new_url)
            # print('new_full_url:', new_full_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return:返回有效数据
        '''
        data={}
        data['url']=page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        #获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary']=summary.get_text()
        return data
#
# from HTMLDownloader import HtmlDownload
#
# dl = HtmlDownload()
# url = 'https://baike.baidu.com/item/%E5%8D%97%E4%BA%AC%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6'
# html = dl.download(url)
# print(html)
# p = HtmlParser()
# urls, data = p.parser(url, html)
# print(len(urls))
# for new_url in urls:
#     print(new_url)
