import json
import re
from .utils import get_page
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup


# 代理网页处理类
class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        # 将字符串str当成有效的表达式来求值并返回计算结果
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=20):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            soup = BeautifulSoup(html, 'lxml')
            for i, child in enumerate(soup.find(id='main').tr.next_siblings):
                # print(child)
                soup1 = BeautifulSoup(str(child), 'lxml')
                for child1 in enumerate(soup1.children):
                    # print(child1)
                    soup2 = BeautifulSoup(str(child1), 'lxml')
                    ip = soup2.td.get_text()
                    port = soup2.td.next_sibling.get_text()
                    print(ip, port)
                    yield ':'.join([ip, port])
        print('daili66的数据获取完成！')
            # print(html)
            # if html:
            #     doc = pq(html)
            #     trs = doc('.containerbox table tbody tr:gt(0)').items()
            #     print(len(list(trs)))
            #     print(trs)
            #     for tr in trs:
            #         ip = tr.find('td:nth-child(1)').text()
            #         if ip == 'ip':
            #             continue
            #         port = tr.find('td:nth-child(2)').text()
            #         print('获取到IP')
            #         print(ip)
            #         yield ':'.join([ip, port])

    # def crawl_proxy360(self):
    #     """
    #     获取Proxy360
    #     :return: 代理
    #     """
    #     start_url = 'http://www.proxy360.cn/Region/China'
    #     print('Crawling', start_url)
    #     html = get_page(start_url)
    #     if html:
    #         doc = pq(html)
    #         lines = doc('div[name="list_proxy_ip"]').items()
    #         for line in lines:
    #             ip = line.find('.tbBottomLine:nth-child(1)').text()
    #             port = line.find('.tbBottomLine:nth-child(2)').text()
    #             yield ':'.join([ip, port])
    #     print('360的数据获取完成')
    #
    # def crawl_goubanjia(self):
    #     """
    #     获取Goubanjia
    #     :return: 代理
    #     """
    #     start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
    #     html = get_page(start_url)
    #     if html:
    #         doc = pq(html)
    #         tds = doc('td.ip').items()
    #         for td in tds:
    #             td.find('p').remove()
    #             yield td.text().replace(' ', '')
    #     print('狗搬家的数据获取完成')
    #
    # def crawl_ip181(self):
    #     start_url = 'http://www.ip181.com/'
    #     html = get_page(start_url)
    #     ip_address = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    #     # \s* 匹配空格，起到换行作用
    #     re_ip_address = ip_address.findall(html)
    #     for address, port in re_ip_address:
    #         result = address + ':' + port
    #         yield result.replace(' ', '')
    #     print('181的数据获取完成')

    def crawl_ip3366(self):
        for page in range(1, 20):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s * 匹配空格，起到换行作用
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')
        print('3366的数据获取完成')

    # def crawl_premproxy(self):
    #     for i in ['China-01', 'China-02', 'China-03', 'China-04', 'Taiwan-01']:
    #         start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(i)
    #         html = get_page(start_url)
    #         if len(str(html)) > 100:
    #             ip_address = re.compile('<td data-label="IP:port ">(.*?)</td>')
    #             re_ip_address = ip_address.findall(html)
    #             for address_port in re_ip_address:
    #                 yield address_port.replace(' ', '')
    #         else:
    #             print(start_url, '暂无数据')

    def crawl_xroxy(self):
        for i in ['CN', 'TW']:
            start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(i)
            html = get_page(start_url)
            if html:
                ip_address1 = re.compile("title='View this Proxy details'>\s*(.*).*")
                re_ip_address1 = ip_address1.findall(html)
                ip_address2 = re.compile("title='Select proxies with port number .*'>(.*)</a>")
                re_ip_address2 = ip_address2.findall(html)
                for address, port in zip(re_ip_address1, re_ip_address2):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')
        print('prem的数据获取完成')

    def crawl_kuaidaili(self):
        for i in range(1, 20):
            start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(start_url)
            if html:
                ip_address = re.compile('<td data-title="IP">(.*?)</td>')
                re_ip_address = ip_address.findall(html)
                port = re.compile('<td data-title="PORT">(.*?)</td>')
                re_port = port.findall(html)
                for address, port in zip(re_ip_address, re_port):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')
        print('快代理的数据获取完成')

    def crawl_xicidaili(self):
        for i in range(1, 20):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie': 'free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host': 'www.xicidaili.com',
                'Referer': 'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests': '1',
            }
            html = get_page(start_url, op=headers)
            if html:
                find_trs = re.compile('<tr class.*?>(.*?)</tr>', re.S)
                trs = find_trs.findall(html)
                for tr in trs:
                    find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                    re_ip_address = find_ip.findall(tr)
                    find_port = re.compile('<td>(\d+)</td>')
                    re_port = find_port.findall(tr)
                    for address, port in zip(re_ip_address, re_port):
                        address_port = address + ':' + port
                        yield address_port.replace(' ', '')
        print('西刺的数据获取完成')

    # def crawl_iphai(self):
    #     start_url = 'http://www.iphai.com/'
    #     html = get_page(start_url)
    #     if html:
    #         find_tr = re.compile('<tr>(.*?)</tr>', re.S)
    #         trs = find_tr.findall(html)
    #         for s in range(1, len(trs)):
    #             find_ip = re.compile('<td>\s+(\d+\.\d+\.\d+\.\d+)\s+</td>', re.S)
    #             re_ip_address = find_ip.findall(trs[s])
    #             find_port = re.compile('<td>\s+(\d+)\s+</td>', re.S)
    #             re_port = find_port.findall(trs[s])
    #             for address, port in zip(re_ip_address, re_port):
    #                 address_port = address + ':' + port
    #                 yield address_port.replace(' ', '')
    #     print('iphai的数据获取完成')

    # def crawl_89ip(self):
    #     start_url = 'http://www.89ip.cn/apijk/?&tqsl=1000&sxa=&sxb=&tta=&ports=&ktip=&cf=1'
    #     html = get_page(start_url)
    #     if html:
    #         find_ips = re.compile('(\d+\.\d+\.\d+\.\d+:\d+)', re.S)
    #         ip_ports = find_ips.findall(html)
    #         for address_port in ip_ports:
    #             yield address_port
    #     print('89的数据获取完成')

    def crawl_data5u(self):
        start_url = 'http://www.data5u.com/free/gngn/index.shtml'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=47AA0C887112A2D83EE040405F837A86',
            'Host': 'www.data5u.com',
            'Referer': 'http://www.data5u.com/free/index.shtml',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        }
        html = get_page(start_url, op=headers)
        if html:
            ip_address = re.compile('<span><li>(\d+\.\d+\.\d+\.\d+)</li>.*?<li class=\"port.*?>(\d+)</li>', re.S)
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')
        print('5u的数据获取完成')