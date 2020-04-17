import requests
from lxml import etree
import random 

class crawler:
    def __init__(self):
        self.start_urls = ""
        self.baseUrl = "https://forum.gamer.com.tw/B.php?page=%s&bsn=30861&subbsn=%s" 
        self.user_agents = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                 "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3" ]

        self.headers = {"User-Agent":random.choice(self.user_agents)}

        self.areaList = {"全部主題":0, "綜合討論":1,"瑪娜回收":2, "攻略心得":3, "日服公會":4, "台版專區":5,
            "日服專區":6, "版友創作":7, "集中討論":8, "板物公告":9, "社群交流":10, "食殿公會":11, 
             "抱怨小屋":12, "遊戲實況":13, "設備問題":14,"劇情討論":15, "陸板專區":16, "陸服公會":17, 
             "外掛專區":18, "真布公會":19, "破曉公會":20, "韓板專區":21}
        self.information = """
                          **************test****************
                          """
    def get_url(self,name):
        print("全部主題, 綜合討論,瑪娜回收, 攻略心得, 日服公會, 台版專區, 日服專區, 版友創作",
            "集中討論, 板物公告, 社群交流, 食殿公會, 抱怨小屋, 遊戲實況, 設備問題",
            "劇情討論, 陸板專區, 陸服公會, 外掛專區, 真布公會, 破曉公會, 韓板專區")
        page = 1
        # area = input("請輸入要訪問那一個討論區？")

        # if area in self.areaList:
        #     addArea = self.areaList[area]
        # else:
        #     print("--------查無此討論區，自動導向「全部主題」討論區--------")
        #     addArea = 0
        if name in self.areaList:
            addArea = self.areaList[name]
        else:
            print("--------查無此討論區，自動導向「全部主題」討論區--------")
            addArea = 0        	

        start_urls = self.baseUrl %(str(page),str(addArea))

        res = requests.get(start_urls, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text

    #     self.crawl_redive(html)

    # def crawl_redive(self,html):
        parsehtml = etree.HTML(html)
        total =  parsehtml.xpath('//tr/td[@class="b-list__main"]/a/div[2]')   
        xStr = ""

        for sing in total :
            baseNameURL = "https://forum.gamer.com.tw/"
            addNameURL = sing.xpath('./div/p/@href')
            

            names = sing.xpath('./div/p/text()')

            for name, nameURL in zip(names, addNameURL):
                nameURL = baseNameURL + str(addNameURL[0])
                title = "標題: " + name
                hyperlink = "連結: " + nameURL
                articleStr = "\n".join([title, hyperlink])
                xStr += articleStr + "\n" + ("=="*40) + "\n"
        # print(xStr)
       	return xStr[10]
                # print("=="*20)
                # print(name,nameURL)
                # print("=="*20)

# if __name__ == "__main__":
#     spider = crawler()
#     spider.get_url("綜合討論")
