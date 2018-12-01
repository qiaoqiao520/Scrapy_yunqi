# Scrapy_yunqi
用scrapy框架爬取云起小说网

## 标签
python、scrapy、sqlite

## 文件说明
debug.py 运行文件
spiders/yunqi.py  项目核心文件
items.py  配置项目中item对象信息
pipelines.py  存储数据文件，存储到数据库或Excel表格中
settings.py  项目的配置文件


## 运行
1.在所需包都下载好，可以运行的情况下，打开debug.py文件右键运行
2.打开pycharm终端控制台，输入 scrapy crawl yunqi --nolog
#### 说明
注：1.--nolog是为了清除你不需要的日志信息，如果需要调试bug的话，最好不要加这句话，在日志中可以查找错误信息。
    2..idea文件在项目运行的时候会自动生成。
