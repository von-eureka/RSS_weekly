import feedparser
from datetime import datetime, timedelta
import time
from bs4 import BeautifulSoup
import ssl

#绕过SSL证书安全认证
ssl._create_default_https_context = ssl._create_unverified_context

# 输出文件路径
raw_file_path = 'raw.md'  # 原始文件路径(修改为你想要输出的目标路径)

# 初始化Markdown内容
markdown_content = ""

# 获取当前日期和一周前的日期
current_date = datetime.now()
one_week_ago = current_date - timedelta(days=7)


# RSS URL & titles（前者为你想订阅的RSS源地址，后者为你标注的RSS title，用来之后分类）
rss_urls = [
    'https://aws.amazon.com/about-aws/whats-new/recent/feed/',
    'https://azurecomcdn.azureedge.net/en-us/updates/feed/?category=databases',
    'https://cloud.google.com/feeds/gcp-release-notes.xml'
]
rss_titles = {
    'https://aws.amazon.com/about-aws/whats-new/recent/feed/': 'AWS',
    'https://azurecomcdn.azureedge.net/en-us/updates/feed/?category=databases': 'Azure',
    'https://cloud.google.com/feeds/gcp-release-notes.xml': 'GCP'
}

# 定义相关关键词（将你想要了解的信息关键词填写到这里）
database_keywords = ['Amazon Aurora', 'Amazon RDS', 'Amazon Redshift', 'Amazon DynamoDB', 'Amazon Elasticache', 'Amazon MemoryDB for Redis', 'Amazon DocumentDB', 'Amazon Keyspaces', 'Amazon Neptune', 'Amazon Timestream', 'Amazon QLDB',#亚马逊数据库产品
                     'Azure SQL','Azure Cosmos DB','Azure SQL Database','Azure Database for PostgreSQL','Azure SQL Managed Instance','Azure Database for MySQL','SQL Server on Azure Virtual Machines','Azure Cache for Redis','Azure Database Migration Service','Azure Managed Instance for Apache Cassandra','Azure Database for MariaDB',#微软数据库产品
                     'Cloud SQL','AlloyDB for PostgreSQL',' Cloud Spanner','BigQuery','Cloud Bigtable',' Firestore','Firebase Realtime Database','MongoDB Atlas','Google Cloud Partner Services'#谷歌数据库产品
                    ]

# 定义日期属性名称列表（注意，这里需要指定rss日期获取位置，如不了解，可用analyse feed.py对rss源进行解析）
date_attributes = ['published_parsed', 'updated_parsed', 'lastBuildDate']

# 初始化发布日期为None
published_date = None

# 在代码中维护一个已处理文章链接的集合
processed_links = set()

# 初始化进度信息
total_paragraphs = 1
got_paragraphs = 0

# 初始化一个字典，用于按RSS标题分类的新闻
rss_keyword_news_dict = {}

# 获取RSS数据
for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    # 获取对应的标题
    rss_title = rss_titles.get(rss_url, "Other")

    # 初始化一个字典，用于按关键词分组的新闻
    keyword_news_dict = {keyword: [] for keyword in database_keywords}

    # 遍历每篇文章并将标题、日期、内容和链接写入Markdown内容
    for entry in feed.entries:
        # 检查是否存在发布日期属性
        for attribute in date_attributes:
            if hasattr(entry, attribute):
                timestamp = getattr(entry, attribute)
                published_date = datetime.fromtimestamp(time.mktime(timestamp))

                # 检查文章是否在最近一周内发布
                if published_date >= one_week_ago:
                    #这里我们使用了谷歌作为RSS推送周报月报的代表，但是最终输出的markdown文件中谷歌部分的格式可能不太工整
                    if  'cloud.google.com' in rss_url:
                        soup = BeautifulSoup(entry.summary, 'html.parser')
                        content = soup.get_text()
                        #这里我们以.来分割文本，你可以根据你的RSS进行修改
                        info_list = content.split('.')
                        contains_keywords = []
                        for sentence in info_list:
                             for keyword in database_keywords:
                                if keyword.lower() in sentence.lower():
                                    contains_keywords.append(sentence)
                                    link = entry.link
                                    keyword_news_dict[keyword].append({
                                                                    'Title': sentence,
                                                                    'Link': link
                                                                })
                    else:
                            title = entry.title
                            # 或者使用 entry.description，具体取决于RSS源的结构
                            content = entry.summary
                            # 提取文章链接
                            link = entry.link
                         # 检查文章标题或内容是否包含关键词
                            contains_keywords = [keyword for keyword in database_keywords if
                                        keyword.lower() in title.lower() or keyword.lower() in content.lower()]
                            # 如果包含关键词，处理输出
                            if contains_keywords:
                                for keyword in contains_keywords:
                                    # 将文章信息添加到关键词分组的字典中
                                    keyword_news_dict[keyword].append({
                                        'Title': title,
                                        'Link': link
                                    })
                   # 检查链接是否已处理过，如果已处理过则跳过
                    if link in processed_links:
                        continue
                    # 标记链接为已处理
                    processed_links.add(link)

                    # 将日期信息格式化为字符串
                    formatted_date = published_date.strftime("%Y-%m-%d")
                    # 增加分段段落的计数
                    got_paragraphs += 1
                    total_paragraphs += 1  # 增加total_paragraphs的值

                    # 打印进度信息
                    progress = (got_paragraphs / total_paragraphs) * 100
                    print(f"Progress: ({got_paragraphs}/{total_paragraphs})")

                    # 将关键词分组的字典添加到相应的RSS标题分类的字典中
                    rss_keyword_news_dict[rss_title] = keyword_news_dict

    # 保存为Markdown文件
    with open(raw_file_path, 'w', encoding='utf-8') as markdown_file:
        for rss_title, keyword_dict in rss_keyword_news_dict.items():
            markdown_file.write(f'## {rss_title}\n\n')  # 写入 RSS 标题
            for keyword, news_list in keyword_dict.items():
                if news_list:
                    markdown_file.write(f'{keyword.capitalize()}:\n\n')  # 写入关键词标题
                    for news in news_list:
                        # 写入新闻标题、内容和链接
                        markdown_file.write(f"*  {news['Title']} [Reference]({news['Link']})\n\n")
                        #markdown_file.write(f"\n\n")

print(f"转换完成，并保存为Markdown文件: {raw_file_path}")




