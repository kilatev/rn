import feedparser

from dateutil.parser import *
from dateutil.tz import *
from datetime import *

from django.conf import settings

from riganinja.models import Channel, Item



class RSSTools(object):

    def __init__(self, lang):
        self.lang = lang

    def get_feed_url(self):
        return settings.RSS_URLS[self.lang]

    def get_parsed_results(self):
        feed_url = self.get_feed_url()
        parsed = feedparser.parse(feed_url)
        # title = parsed['entries'][0]['description']
        # title_utf = title.encode('utf-8', 'replace')
        # print title_utf
        # with open('aaa.txt', 'w') as fi:
        #     fi.write(title_utf)
        return parsed

    def create_channel(self, parsed):

        updated =  parse(parsed.feed.updated)
        data = {
            'title': parsed.feed.title,
            'link': parsed.feed.link,
            'description': parsed.feed.description,
            'lastBuildDate': updated,
            'generator': parsed.feed.generator,
            'language': parsed.feed.language
        }
        ch = Channel.objects.create(**data)
        return ch

    def parsed_to_model(self, parsed):
        channel = Channel.objects.filter(link=parsed.feed.link)
        if not channel:
            channel = self.create_channel(parsed)
        items = []
        for entry in parsed.entries:
            published = parse(entry.published)
            data={
                'title': entry.title,
                'link': entry.link,
                'guid': entry.guid,
                'description': entry.description,
                'author': entry.author,
                'category': entry.category,
                'pubDate': published,
                'channel': channel,
            }
            item = Item(**data)
            items.append(item)
        Item.objects.bulk_create(items)