# RSS_weekly
## 这是什么？
一个小小的程序，能将你添加的rss源生成markdown格式的周报。

## 我能得到什么？
一份markdown格式的周报：   

![AWS weekly](https://github.com/von-eureka/RSS_weekly/assets/82219377/195e02fd-366a-462d-8498-d68bd8e71f79)
* 按照时间范围与关键词对RSS源消息进行筛选
* 将RSS源信息按照“RSS标题-关键词”二级结构进行分类
* 直接生成上图格式的markdown文件
## 如何使用？
首先安装`feedparser` `beautifulsoup4`包   

其次在**rss_weekly.py**中完善以下参数
* `raw_file_path`:周报输出的位置
* `rss_urls`:从哪些rss源获取周报信息
* `rss_titles`：标题，将来自不同rss源的信息进行分类
* `database_keywords`:关键词，可以用来过滤你想在周报里看到的信息
* `date_attributes`:周报获取rss源日期的位置，这里需要使用来对rss地址进行解析来获得。

  >如果你不清楚你所订阅的rss源日期位置是哪个，那就修改**analyse feed.py**中的rss_url并运行，便可看到解析后的rss源。

  >如果还不清楚，那就将解析后的rss源直接全部拷贝下来塞到chatgpt中，让他告诉你日期位置在哪里。

所有参数设置完毕后运行**rss_weekly.py**即可。
>上传的**rss_weekly.py**以AWS、Azure、GCP数据库更新为例填写了相关参数，在网络畅通的情况下，修改周报输出位置后运行便可得到一份数据库更新周报。
## 如何实现？
利用feedparser读取rss源，并对rss源的日期属性进行检测，搜集rss源一周内发布的信息，并记录rss源信息的标题与日期;有些rss源发布的是周报或者月报，在标明后会使用bs4对rss源进行文本提取，随后根据指定特征对文本进行分割。最后，程序会根据关键词库检索含有关键词的信息，并输出为markdown文件。

## 运行环境
### OS
windows：windows11已测试，可正常运行
macOS:在macOS上需进行以下操作：
* 打开访达>应用程序>python3.x（3.x为你安装的python版本号）>运行Install Certificates.command即可
> 如没有此文件，参考:
> 
> https://stackoverflow.com/questions/44649449/brew-installation-of-python-3-6-1-ssl-certificate-verify-failed-certificate/44649450#44649450

* 如上述方案不能解决，请下载**rss_weekly(SSL).py**
> **注意！非常不推荐这样做，除非您绝对信任您添加的网站，这可能会带来巨大的安全问题，其原理为绕过SSL证书认证。**
  


### Requirements
* python3
* 需要`feedparser` `beautifulsoup4`包
## 更新计划
* 更简洁的代码
* UI
* Requirements.txt
