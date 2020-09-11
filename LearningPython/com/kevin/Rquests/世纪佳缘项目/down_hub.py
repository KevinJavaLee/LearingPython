"""
@File    : down_hub.py
@Time    : 2020/9/7 11:06
@Author  : KevinXiao
@Software: PyCharm
"""

import os
import re
import requests




class Pornhub():
    def __init__(self, url):
        self.url = url
        self.rootpath = down_path + "/"

    def parse_html(self, url):
        resp = requests.get(url, headers=random_header(), timeout=30)
        print(resp.text)
        return resp.text


    def save_mp4(self, item):
        if item["quality_720p"]:
            url = item["quality_720p"]
        else:
            url = item["quality_480p"]
        file_path = self.rootpath + re.sub(r"[/\\:*?\"<>|]", "_", item["video_title"]) + ".mp4"
        self.download_from_url(url, file_path, random_header())

    def download_from_url(self, url, filepath, headers):
        print("开始下载:", filepath)
        with open(filepath, 'wb') as f:
            f.write(requests.get(url, headers,timeout=30).content)

    def run(self):
        try:
            print("运行run")
            url = self.url
            html_str = self.parse_html(url)
            item = {}
            item["video_title"] = re.findall('"video_title":"(.*?)",', html_str)[0]
            item["quality_720p"] = re.findall('"quality_720p":"(.*?)",', html_str)
            if item['quality_720p']:
                item["quality_720p"] = item["quality_720p"][0].replace('\\', '')
            item["quality_480p"] = re.findall('"quality_480p":"(.*?)",', html_str)
            if item['quality_480p']:
                item["quality_480p"] = item["quality_480p"][0].replace('\\', '')
            print("结束run")
            self.save_mp4(item)
        except Exception as e:
            print(e)


down_path = "D:/ph/other"


def random_header():
    return {
        'cookie': "bs=1kfg8xrm4urlktibwj1see2s7gxv8ull; ss=416954180971255585; _ga=GA1.2.328524346.1593437024; APUnique2_3=2286329247; platform_cookie_reset=pc; fg_9d12f2b2865de2f8c67706feaa332230=84889.100000; lang=cn; platform=pc; ua=0d7547ea912e3ce2a35572c8b9a755b1; _gid=GA1.2.384990218.1599447854",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }


download_urls = [
    "https://cn.pornhub.com/view_video.php?viewkey=ph5f1b0bab6cab7",
    "https://cn.pornhub.com/view_video.php?viewkey=ph5f06f3476c628"

]

if __name__ == '__main__':
    if not os.path.exists(down_path):
        os.makedirs(down_path)
    print("读取存放目录为:", down_path)
    try:
        print("将要爬取的链接为:")
        for url in download_urls:
            print(url)
        for url in download_urls:
            p = Pornhub(url)
            p.run()

    except Exception as e:
        print("\n*" * 20)
        print("程序运行错误:", e)
        print("*" * 20, "\n")
    else:
        print("QQ: 2416447718")
        print("QQ: 2470571458")
        print("TG: @porsms")
        # https://cn.pornhub.com/view_video.php?viewkey=ph5f06f3476c628