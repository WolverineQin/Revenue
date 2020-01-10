import requests
from lxml import html
import use_api as api
from bs4 import BeautifulSoup
import re
import json
import csv

class CZSR:
    def __init__(self):
        pass

    def get_ip(self):
        ip = api.get_proxy()
        return ip

    def get_page(self,url):
        ip = self.get_ip()
        proxies = {
            "http:": str("http://" + str(ip))
        }
        headers = {
            "Cookie": " production.flex.admin.sid=s%3AMmcJPdDwO38s98RHFKhIEO6wGZfe1vfg.0rsNoSQ8Wo6jB%2BIw7gSxAfpOa4Q%2BZkfIgmt2%2FOIV5Sc; _ga=GA1.2.2033915219.1577152058; _gid=GA1.2.909002081.1577152058; driftt_aid=cb8715a6-416f-40a6-bf27-300043579e91; DFTT_END_USER_PREV_BOOTSTRAPPED=true; wisepops_visits=%5B%222019-12-25T02%3A46%3A00.215Z%22%2C%222019-12-24T08%3A33%3A03.891Z%22%2C%222019-12-24T01%3A47%3A54.087Z%22%5D; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%22187094%22%3A%7B%22dc%22%3A2%2C%22d%22%3A%222019-12-25T02%3A46%3A07.220Z%22%7D%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A7%2C%22cid%22%3A%2241374%22%2C%22v%22%3A4%7D; wisepops_session=%7B%22arrivalOnSite%22%3A%222019-12-25T02%3A46%3A00.215Z%22%2C%22mtime%22%3A%222019-12-25T02%3A46%3A07.221Z%22%2C%22pageviews%22%3A1%2C%22popups%22%3A%7B%22187094%22%3A0%7D%2C%22src%22%3Anull%2C%22utm%22%3A%7B%7D%7D; _gat_UA-5362499-1=1; AWSALB=geZlTVgFCA2p8NeQKMMg98iA9ej45U9Y5Jr6xa0WvD1ilrzFaMA7pTmsUXIRNnTpcEHG6M2YKjmonkieUFkbyrydjd3jE8U6uSHYsuN9s3bEFYQt95stnDQvnSs9k64i9gtgb9QoUpqIbNHXuNu9u1QAPZa4pGS+fSot8P1DXJmi6yZnbOsZ3EowA5Bcmg==; __z_a=2936487248182051445418205; driftt_sid=83ba6108-f7de-4ff4-97fd-5b22ea210a76",
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
        }
        try:
            page = requests.get(url,headers=headers,proxies=proxies)
            if page.status_code == 200:
                return page
            else:
                print(page.status_code)
        except Exception as e:
            print(e)

    def get_data_page(self,url):
        ip = self.get_ip()
        proxies = {
            "http:": str("http://" + str(ip))
        }
        headers = {
            "Cookie": "production.flex.admin.sid=s%3AMmcJPdDwO38s98RHFKhIEO6wGZfe1vfg.0rsNoSQ8Wo6jB%2BIw7gSxAfpOa4Q%2BZkfIgmt2%2FOIV5Sc; _ga=GA1.2.2033915219.1577152058; _gid=GA1.2.909002081.1577152058; driftt_aid=cb8715a6-416f-40a6-bf27-300043579e91; DFTT_END_USER_PREV_BOOTSTRAPPED=true; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%22187094%22%3A%7B%22dc%22%3A2%2C%22d%22%3A%222019-12-25T02%3A46%3A07.220Z%22%7D%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A7%2C%22cid%22%3A%2241374%22%2C%22v%22%3A4%7D; wisepops_visits=%5B%222019-12-25T03%3A10%3A53.983Z%22%2C%222019-12-25T02%3A47%3A45.069Z%22%2C%222019-12-25T02%3A46%3A00.215Z%22%2C%222019-12-24T08%3A33%3A03.891Z%22%2C%222019-12-24T01%3A47%3A54.087Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222019-12-25T03%3A10%3A53.983Z%22%2C%22mtime%22%3A%222019-12-25T03%3A10%3A53.987Z%22%2C%22pageviews%22%3A1%2C%22popups%22%3A%7B%22187094%22%3A2%7D%2C%22src%22%3Anull%2C%22utm%22%3A%7B%7D%7D; AWSALB=ek2y1GRZ6XL8dLIQCW1U0PPudRBBTHIMmLYVij8GZ4grUcleTzozpqfi8ykAilW8yIeEyFSW/oK3w2/9Nw/bI6PLbZdDBHmflWUx0vZM/XpL//7+dtBXdtGriGh6AvmP4bW0YOUOyIYML9MXh12BuSA7heMDSprQefl4uXdZFxgIxH1wgxoZWjuX3tMWsA==",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
        }
        try:
            page = requests.get(url,headers=headers,proxies=proxies)
            if page.status_code == 200:
                return page
            else:
                print(page.status_code)
        except Exception as e:
            print(e)

    def get_urllist(self,url):
        page = self.get_page(url)
        page.encoding = 'utf-8'
        data_str = page.text
        data = json.loads(data_str)
        html = data["html"]
        patten = re.compile('XXX的财政收入:(.*?)在.*?\"image\":\"(.*?)",',flags=re.DOTALL)
        urllist = patten.findall(html)
        if len(urllist) != 0:
            return urllist
        else:
            print("Get the URL fail!")

    def get_data(self,url):
        page = self.get_data_page(url)
        page.encoding = 'utf-8'
        data = page.text
        etree = html.etree
        selector = etree.HTML(data)
        result = []
        for i in range(4,13):
            patten = '/html/body/svg/g[6]/g[' + str(i) +']/text/tspan[2]/text()'
            r = selector.xpath(patten)
            result.extend(r)
        if len(result) != 0:
            return result
        else:
            print("Get the result fail")

    def write_to_csv(self,result):
        with open('E:\公司资料\大数据实验室\xxxxxx\财政收入/czsr.csv','a',newline='',errors="ignore",encoding='gb2312') as csvfile:
            filename = ['X','X','2010','2011','2012','2013','2014','2015','2016','2017','2018']
            writer = csv.DictWriter(csvfile,fieldnames=filename)
            # writer.writeheader()
            result_dict = dict(map(lambda x, y: [x, y], filename, result))
            writer.writerow(result_dict)

if __name__ == '__main__':
    for p in range(12,30):
        url_base = 'https://xxxxxx?page='+str(p)
        czsr = CZSR()
        urllist = czsr.get_urllist(url_base)
        for i in range(0,len(urllist)):
            print("正在存储第%s页第%s个数据" % (p,i+1))
            result = czsr.get_data(urllist[i][1])
            if urllist[i][0].find(":") != -1:
                sheng = urllist[i][0].split(':')[0]
                shi = urllist[i][0].split(':')[1]
            else:
                sheng = ''
                shi = urllist[i][0]
            result.insert(0,sheng)
            result.insert(1,shi)
            czsr.write_to_csv(result)
            print(result)
            print("存储第%s页第%s个数据完成" % (p, i + 1))
