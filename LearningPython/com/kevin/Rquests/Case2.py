"""
@File    : Case2.py
@Time    : 2020/7/22 20:47
@Author  : KevinXiao
@Software: PyCharm
"""

# 案例二：爬取亚马逊的商品信息
import  requests


try:
# 爬取地址
    # 设置请求头
    kv = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    # 请求的地址
    url ="https://www.amazon.cn/gp/product/B08C2C1FBM/ref=s9_acss_bw_cg_editor_2c1_w?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-5&pf_rd_r=DTEQSGEGTSB38TRSAZDJ&pf_rd_t=101&pf_rd_p=05e779ba-2be7-4b31-b7f7-ac970eb58af6&pf_rd_i=116169071"
    req = requests.get(url,timeout= 30,headers=kv)
    req.encoding = req.apparent_encoding
    # req.raise_for_status()
    print(req.request.headers)
except:
    print("出现异常")
else:
    if req.status_code == 200:
        print(req.text[:1000])
    else:
        print(req.status_code)

