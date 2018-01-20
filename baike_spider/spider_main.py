#encoding:utf8

from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer


class SpiderMain(object):
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    # 爬虫方法    
    def craw(self, root_url):
        count = 1
        # 管理器的方法
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url) 
                # 下载器的方法
                html_cont = self.downloader.download(new_url)
                # 解析器的方法(注意此方法的返回值)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 管理器添加新url的方法
                self.urls.add_new_urls(new_urls)
                
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
                
            except:
                print 'craw failed'    
            
            
        self.outputer.output_html()
            
    
    


# 入口，类似C语言的main函数
if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)