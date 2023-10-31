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
1、下载requirements.txt  rss_weekly，视情况下载rsss_weekly(SSL)和analyse feed；

2、配置依赖项：在终端中切换到你下载requirements.txt的位置，运行：

`pip install -r requirements.txt`

3、使用代码编辑器打开rss_weekly.py，
在**rss_weekly.py**中完善以下参数
* `raw_file_path`:周报输出的位置
* `rss_urls`:从哪些rss源获取周报信息
* `rss_titles`：标题，将来自不同rss源的信息进行分类
* `database_keywords`:关键词，可以用来过滤你想在周报里看到的信息
* `date_attributes`:周报获取rss源日期的位置，这里需要使用来对rss地址进行解析来获得。
所有参数设置完毕后运行**rss_weekly.py**即可。
>上传的**rss_weekly.py**以AWS、Azure、GCP数据库更新为例填写了相关参数，在网络畅通的情况下，修改周报输出位置后运行便可得到一份数据库更新周报。

## 可选项
**analyse feed.py**:当你不清楚你想订阅的rss源日期位置在哪里时，你可以使用代码编辑器将analyse feed.py中的`rss_url`改成你想知道的rss源，随后运行，脚本会返回给你解析后的rss源，找到包含有日期的标签名即可，如果真的找不到，可以将解析后的内容全部复制下来扔到chatgpt或者newbing中询问；

**rss_weekly(SSL).py**：参见**运行环境**
## 如何实现？
利用feedparser读取rss源，并对rss源的日期属性进行检测，搜集rss源一周内发布的信息，并记录rss源信息的标题与日期;有些rss源发布的是周报或者月报，在标明后会使用bs4对rss源进行文本提取，随后根据指定特征对文本进行分割。最后，程序会根据关键词库检索含有关键词的信息，并输出为markdown文件。

## 运行环境
### OS
windows：windows11已测试，可正常运行

macOS: 在macOS上需进行以下操作：
* 打开访达>应用程序>python3.x（3.x为你安装的python版本号）>运行Install Certificates.command >随后正常配置依赖项，使用代码编辑器打开rss_weekly.py，按照上文提到的完善相关参数即可
> 如没有此文件，参考:
> 
> https://stackoverflow.com/questions/44649449/brew-installation-of-python-3-6-1-ssl-certificate-verify-failed-certificate/44649450#44649450

* 如上述方案不能解决，请下载**rss_weekly(SSL).py**，随后配置依赖项，并在rss_weekly(SSL).py中进行相关参数修改，之后运行。【rss_weekly(SSL).py和rss_weekly.py需要完善的参数是一样的】
> **注意！非常不推荐这样做，除非您绝对信任您添加的网站，这可能会带来巨大的安全问题，其原理为绕过SSL证书认证。**
  

## 更新计划
* 更简洁的代码
* UI
