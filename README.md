# 功能
使用scrapy来爬取实习僧的全站职位数据

# 环境
scrapy

# 运行
dos下cd到scrapy.cfg所在目录，输入scrapy crawl shixiseng

# 说明
1、没有使用代理抓取，所以只开启了16个线程，每个url访问间隔为0.5秒  
2、运行了一个多小时，正常结束，获取到8万多条数据  
3、数据存储在mongodb的shixiseng.info
4、导出的CSV数据：https://www.lanzous.com/i3uvkva

# 实习僧反爬处理
https://blog.csdn.net/Qwertyuiop2016/article/details/89432868

# scrapy教程
https://blog.csdn.net/Qwertyuiop2016/article/details/89416200

# 联系方式
CSDN：https://blog.csdn.net/Qwertyuiop2016/article/details/89226209  
Email：kanade@blisst.cn  
GitHub: https://github.com/kanadeblisst/ShiXiSengSpider