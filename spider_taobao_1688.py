# -*- coding: utf-8 -*-
# @file : spider_1688_business.py
# -*- coding: utf-8 -*-
# @file : spider_1688.py
# -*- coding: utf-8 -*-
import json
import time
from selenium import webdriver
from lxml import etree
import requests
from Config.DBConfig import Connection
proxy_ips = 'xxxxx'



class Spider1688(object):
    def __init__(self, host="xxxx", user="xxxx", password="xxxx", database="xxx", chromedriver_path='chromedriver.exe'):
        self.conn = Connection(host=host, user=user, password=password, database=database, charset="utf8")
        self.url = 'https://show.1688.com/pinlei/industry/factory.html?cms_id=228075&&sceneSetId=840&sceneId=1565&bizId=3811'
        # self.url = 'https://www.douyin.com/'
        options = webdriver.ChromeOptions()
        pro_ip = proxy_ips
        options.add_argument(('--proxy-server=' + pro_ip))
        # options.AddArguments("--incognito", "--disable-blink-features=AutomationControlled");
        # options.add_experimental_option("--incognito", "--disable-blink-features=AutomationControlled")
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')
        # 引用header头
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片，加快访问速度
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_experimental_option('useAutomationExtension', False)
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)  # 接收传入的 chromedriver地址 和设置好的 options
        # Canvas指纹:
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """const toBlob=HTMLCanvasElement.prototype.toBlob;const toDataURL=HTMLCanvasElement.prototype.toDataURL;const getImageData=CanvasRenderingContext2D.prototype.getImageData;function noisify(canvas,context){if(context){const shift={'r':Math.floor(Math.random()*10)-5,'g':Math.floor(Math.random()*10)-5,'b':Math.floor(Math.random()*10)-5,'a':Math.floor(Math.random()*10)-5};const width=canvas.width;const height=canvas.height;if(width&&height){const imageData=getImageData.apply(context,[0,0,width,height]);for(let i=0;i<height;i++){for(let j=0;j<width;j++){const n=((i*(width*4))+(j*4));imageData.data[n+0]=imageData.data[n+0]+shift.r;imageData.data[n+1]=imageData.data[n+1]+shift.g;imageData.data[n+2]=imageData.data[n+2]+shift.b;imageData.data[n+3]=imageData.data[n+3]+shift.a}}window.top.postMessage("canvas-fingerprint-defender-alert",'*');context.putImageData(imageData,0,0)}}}Object.defineProperty(HTMLCanvasElement.prototype,"toBlob",{"value":function(){noisify(this,this.getContext("2d"));return toBlob.apply(this,arguments)}});Object.defineProperty(HTMLCanvasElement.prototype,"toDataURL",{"value":function(){noisify(this,this.getContext("2d"));return toDataURL.apply(this,arguments)}});Object.defineProperty(CanvasRenderingContext2D.prototype,"getImageData",{"value":function(){noisify(this.canvas,this);return getImageData.apply(this,arguments)}});document.documentElement.dataset.cbscriptallow=true;if(document.documentElement.dataset.cbscriptallow!=="true"){const iframes=[...window.top.document.querySelectorAll("iframe[sandbox]")];for(var i=0;i<iframes.length;i++){if(iframes[i].contentWindow){if(iframes[i].contentWindow.CanvasRenderingContext2D){iframes[i].contentWindow.CanvasRenderingContext2D.prototype.getImageData=CanvasRenderingContext2D.prototype.getImageData}if(iframes[i].contentWindow.HTMLCanvasElement){iframes[i].contentWindow.HTMLCanvasElement.prototype.toBlob=HTMLCanvasElement.prototype.toBlob;iframes[i].contentWindow.HTMLCanvasElement.prototype.toDataURL=HTMLCanvasElement.prototype.toDataURL}}}}""", })
        # Webgl指纹:
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """var config={"random":{"value":function(){return Math.random()},"item":function(e){var rand=e.length*config.random.value();return e[Math.floor(rand)]},"number":function(power){var tmp=[];for(var i=0;i<power.length;i++){tmp.push(Math.pow(2,power[i]))}return config.random.item(tmp)},"int":function(power){var tmp=[];for(var i=0;i<power.length;i++){var n=Math.pow(2,power[i]);tmp.push(new Int32Array([n,n]))}return config.random.item(tmp)},"float":function(power){var tmp=[];for(var i=0;i<power.length;i++){var n=Math.pow(2,power[i]);tmp.push(new Float32Array([1,n]))}return config.random.item(tmp)}},"spoof":{"webgl":{"buffer":function(target){var proto=target.prototype?target.prototype:target.__proto__;const bufferData=proto.bufferData;Object.defineProperty(proto,"bufferData",{"value":function(){var index=Math.floor(config.random.value()*arguments[1].length);var noise=arguments[1][index]!==undefined?0.1*config.random.value()*arguments[1][index]:0;arguments[1][index]=arguments[1][index]+noise;window.top.postMessage("webgl-fingerprint-defender-alert",'*');return bufferData.apply(this,arguments)}})},"parameter":function(target){var proto=target.prototype?target.prototype:target.__proto__;const getParameter=proto.getParameter;Object.defineProperty(proto,"getParameter",{"value":function(){window.top.postMessage("webgl-fingerprint-defender-alert",'*');if(arguments[0]===3415)return 0;else if(arguments[0]===3414)return 24;else if(arguments[0]===36348)return 30;else if(arguments[0]===7936)return"WebKit";else if(arguments[0]===37445)return"Google Inc.";else if(arguments[0]===7937)return"WebKit WebGL";else if(arguments[0]===3379)return config.random.number([14,15]);else if(arguments[0]===36347)return config.random.number([12,13]);else if(arguments[0]===34076)return config.random.number([14,15]);else if(arguments[0]===34024)return config.random.number([14,15]);else if(arguments[0]===3386)return config.random.int([13,14,15]);else if(arguments[0]===3413)return config.random.number([1,2,3,4]);else if(arguments[0]===3412)return config.random.number([1,2,3,4]);else if(arguments[0]===3411)return config.random.number([1,2,3,4]);else if(arguments[0]===3410)return config.random.number([1,2,3,4]);else if(arguments[0]===34047)return config.random.number([1,2,3,4]);else if(arguments[0]===34930)return config.random.number([1,2,3,4]);else if(arguments[0]===34921)return config.random.number([1,2,3,4]);else if(arguments[0]===35660)return config.random.number([1,2,3,4]);else if(arguments[0]===35661)return config.random.number([4,5,6,7,8]);else if(arguments[0]===36349)return config.random.number([10,11,12,13]);else if(arguments[0]===33902)return config.random.float([0,10,11,12,13]);else if(arguments[0]===33901)return config.random.float([0,10,11,12,13]);else if(arguments[0]===37446)return config.random.item(["Graphics","HD Graphics","Intel(R) HD Graphics"]);else if(arguments[0]===7938)return config.random.item(["WebGL 1.0","WebGL 1.0 (OpenGL)","WebGL 1.0 (OpenGL Chromium)"]);else if(arguments[0]===35724)return config.random.item(["WebGL","WebGL GLSL","WebGL GLSL ES","WebGL GLSL ES (OpenGL Chromium"]);return getParameter.apply(this,arguments)}})}}}};config.spoof.webgl.buffer(WebGLRenderingContext);config.spoof.webgl.buffer(WebGL2RenderingContext);config.spoof.webgl.parameter(WebGLRenderingContext);config.spoof.webgl.parameter(WebGL2RenderingContext);document.documentElement.dataset.wgscriptallow=true;if(document.documentElement.dataset.wgscriptallow!=="true"){const iframes=[...window.top.document.querySelectorAll("iframe[sandbox]")];for(var i=0;i<iframes.length;i++){if(iframes[i].contentWindow){if(iframes[i].contentWindow.WebGLRenderingContext){iframes[i].contentWindow.WebGLRenderingContext.prototype.bufferData=WebGLRenderingContext.prototype.bufferData;iframes[i].contentWindow.WebGLRenderingContext.prototype.getParameter=WebGLRenderingContext.prototype.getParameter}if(iframes[i].contentWindow.WebGL2RenderingContext){iframes[i].contentWindow.WebGL2RenderingContext.prototype.bufferData=WebGL2RenderingContext.prototype.bufferData;iframes[i].contentWindow.WebGL2RenderingContext.prototype.getParameter=WebGL2RenderingContext.prototype.getParameter}}}}"""})
        # Css字体指纹:
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """var rand={"noise":function(){var SIGN=Math.random()<Math.random()?-1:1;return Math.floor(Math.random()+SIGN*Math.random())},"sign":function(){const tmp=[-1,-1,-1,-1,-1,-1,+1,-1,-1,-1];const index=Math.floor(Math.random()*tmp.length);return tmp[index]}};Object.defineProperty(HTMLElement.prototype,"offsetHeight",{get(){const height=Math.floor(this.getBoundingClientRect().height);const valid=height&&rand.sign()===1;const result=valid?height+rand.noise():height;return result}});Object.defineProperty(HTMLElement.prototype,"offsetWidth",{get(){const width=Math.floor(this.getBoundingClientRect().width);const valid=width&&rand.sign()===1;const result=valid?width+rand.noise():width;return result}});document.documentElement.dataset.fbscriptallow=true;if(document.documentElement.dataset.fbscriptallow!=="true"){const iframes=[...window.top.document.querySelectorAll("iframe[sandbox]")];for(var i=0;i<iframes.length;i++){if(iframes[i].contentWindow){if(iframes[i].contentWindow.HTMLElement){iframes[i].contentWindow.HTMLElement.prototype.offsetWidth=HTMLElement.prototype.offsetWidth;iframes[i].contentWindow.HTMLElement.prototype.offsetHeight=HTMLElement.prototype.offsetHeight}}}}"""})
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

    def all_item(self):
        new_item = {}
        new_item["title_name"] = ""
        new_item["main_business"] = ""
        new_item["factory_type"] = ""
        new_item["factory_address"] = ""
        new_item["business_url"] = ""
        new_item["start_time"] = ""
        new_item["year_money"] = ""
        new_item["company_area"] = ""
        new_item["employee"] = ""
        new_item["play_demo"] = ""
        new_item["machine"] = ""
        new_item["natural_endowments"] = ""
        new_item["proxy_cards"] = ""
        new_item["cards"] = ""
        new_item["certificate"] = ""
        new_item["product_num"] = ""
        new_item["month_value"] = ""
        new_item["special_process"] = ""
        new_item["product_quality_cert"] = ""
        new_item["management_system_cert"] = ""
        new_item["source_time"] = ""
        return new_item


    def rep_str(self, strs):
        if isinstance(strs, list):
            new_str = strs[0].strip()
            new_str = new_str.split('(')[0] if '(' in new_str else new_str
            new_str = new_str.replace('成立时间', 'start_time')
            new_str = new_str.replace('年交易额', 'year_money')
            new_str = new_str.replace('公司面积', 'company_area')
            new_str = new_str.replace('员工总数', 'employee')
            new_str = new_str.replace('支持打样', 'play_demo')
            new_str = new_str.replace('加工设备', 'machine')
            new_str = new_str.replace('外贸资质', 'natural_endowments')
            new_str = new_str.replace('代工品牌', 'proxy_cards')
            new_str = new_str.replace('商标/品牌', 'cards')
            new_str = new_str.replace('资质证书', 'certificate')
            new_str = new_str.replace('生产人数', 'product_num')
            new_str = new_str.replace('月产值', 'month_value')
            new_str = new_str.replace('特殊工艺', 'special_process')
            new_str = new_str.replace('生产质量认证', 'product_quality_cert')
            new_str = new_str.replace('管理体系认证', 'management_system_cert')
            new_str = new_str.replace('原材料采购时间', 'source_time')
            new_str = new_str.replace('供货客户', 'suppler_cum')
        else:
            new_str = strs
        return new_str

    def get_str(self, strs):
        if strs and isinstance(strs, list):
            new_str = strs[0].strip()
        else:
            new_str = ''
        return new_str

    def start_spider(self):
        self.browser.get(self.url)
        time.sleep(5)
        title_content = self.browser.page_source
        rsqlist_html = etree.HTML(title_content)
        factory_item = rsqlist_html.xpath('//div[@class="list"]/div/a/@href')
        for factory_url in factory_item:
            print(factory_url)
            self.browser.get(url=factory_url)
            time.sleep(4)
            factory_source = self.browser.page_source
            factory_html = etree.HTML(factory_source)
            item = self.all_item()
            item['title_name'] = self.get_str(factory_html.xpath('//h1/text()'))
            item['main_business'] = self.get_str(factory_html.xpath('//span[@class="itemText"]/text()'))
            factory_type = self.get_str(factory_html.xpath('//div[@class="facInfo"]/img/@src'))
            item['factory_type'] = factory_type if factory_type else self.get_str(factory_html.xpath('//div[@class="chenItem"]/img/@src'))
            item['factory_address'] = self.get_str(factory_html.xpath('//div[@class="location"]/text()'))
            factory_div_infos = factory_html.xpath('//div[@class="containerbck"]/div[@class="container"]/div/div[not(@class="com_top")]')
            factory_div_infos = factory_div_infos if len(factory_div_infos) > 0 else factory_html.xpath('//div[@class="containerbck"]/div/div[not(@class="com_top")]')
            for factory_div in factory_div_infos:
                div_paths = factory_div.xpath('./div')
                for div_path in div_paths:
                    items = {}
                    div_keys = self.rep_str(div_path.xpath('./div[1]//text()'))
                    div_values = self.rep_str(div_path.xpath('./div[2]//text()'))
                    items[div_keys] = div_values
                    item.update(items)
            self.browser.find_element_by_xpath('//div[contains(@class,"abItem")][2]').click()
            time.sleep(3)
            factory_source = self.browser.page_source
            factory_html = etree.HTML(factory_source)
            product_infos = factory_html.xpath('//div[@class="ability"]/div')
            for product_info in product_infos:
                product_paths = product_info.xpath('./div')
                for product_path in product_paths:
                    items_2 = {}
                    product_keys = self.rep_str(product_path.xpath('./span[1]/text()'))
                    product_values = self.rep_str(product_path.xpath('./span[2]/text()'))
                    items_2[product_keys] = product_values
                    item.update(items_2)
            index_num = len(factory_html.xpath('//div[contains(@class,"abItem")]'))
            self.browser.find_element_by_xpath(f'//div[contains(@class,"abItem")][{index_num}]').click()
            time.sleep(2)
            business_source = self.browser.page_source
            business_html = etree.HTML(business_source)
            business_infos = business_html.xpath('//ul[@class="integrity_info"]/a/@href')
            business_url = ''
            for business_info in business_infos:
                if business_info:
                    business_url = business_info
                    break
            item['business_url'] = business_url
            print(json.dumps(item, ensure_ascii=False))

if __name__ == '__main__':
    s_1688 = Spider1688()
    s_1688.start_spider()
