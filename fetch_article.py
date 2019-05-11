#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 21:27
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : fetch_article.py
from urllib.parse import quote

from config import base_url
from db import db
from libs.httper import make_session
from libs.modify_publish_time import modify_time
from models.article import Article


def save_to_mysql(data, query_zh):
    """
    将每篇文章存在数据库
    :param data:
    :param query_zh:
    :return:
    """
    new_data = eval(data)
    new_data = new_data['data']
    for single in new_data:
        if 'url' in single.keys():
            url = base_url + single['url']
        else:
            url = ''
        publish_time = modify_time(single['published_at'])
        item = {'typ': single['type'], 'publish_time': publish_time, 'title': single['title'],
                'url': url, 'article_id': single['id']}

        item['Compliance'] = 1 if len(item['title']) >= 14 else 0

        try:
            if (
                    # not db.session.query(Article.article_id).filter_by(article_id=item["article_id"]).first()
                    not db.session.query(Article.title).filter_by(title=item["title"]).first()
            ):  # 查不到时，为 None
                with db.auto_commit():
                    db.session.add(Article(**item))
                print("ok...写入成功 ", query_zh)
            else:
                print("exist...数据已存在，不写入数据", query_zh, item["title"])
        except Exception as e:
            print(item)


def fetch():
    # query_list = ['美股', 'A股', '娛樂', '健康']  # '股票', '股市' 國際 歐非 電影
    query_list = ['電影']
    for query in query_list:
        query_zh = query
        query = quote(query)
        # print(query)
        for i in range(1, 2500, 10):
            print(i)
            offset = str(i)
            url6 = 'https://tw.news.yahoo.com/_td-news/api/resource/NewsSearchService;loadMore=true;mrs=%7B%22size%22%3A%7B%22w%22%3A220%2C%22h%22%3A128%7D%7D;offset={};query={};usePrefetch=false?bkt=news-TW-zh-Hant-TW-def&device=desktop&feature=videoDocking&intl=tw&lang=zh-Hant-TW&partner=none&prid=7kpmgr5ed48qc&region=TW&site=news&tz=Asia%2FHong_Kong&ver=2.0.1193&returnMeta=true'.format(
                query, offset
            )
            url7 = 'https://tw.news.yahoo.com/_td-news/api/resource/NewsSearchService;loadMore=true;mrs=%7B%22size%22%3A%7B%22w%22%3A220%2C%22h%22%3A128%7D%7D;offset={};query={};usePrefetch=false?bkt=news-TW-zh-Hant-TW-def&device=desktop&feature=videoDocking&intl=tw&lang=zh-Hant-TW&partner=none&prid=2f21i3led4cbb&region=TW&site=news&tz=Asia%2FHong_Kong&ver=2.0.1193&returnMeta=true'.format(
                query, offset
            )

            session = make_session()
            response = session.get(url6)
            if response.text is None:
                break
            save_to_mysql(response.text, query_zh)


if __name__ == '__main__':
    fetch()
