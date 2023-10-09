import feedparser

# 输入RSS订阅源的URL
rss_url = 'https://cloud.google.com/release-notes'

# 获取RSS数据
feed = feedparser.parse(rss_url)

# 显示整个RSS数据的结构
print(feed)
