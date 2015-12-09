import feedparser

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
        print parsed.feed
        data = {
            'title': parsed.feed.title,
            'link': parsed.feed.link,
            'description': parsed.feed.description,
            'lastBuildDate': parsed.feed.updated,
            'generator': parsed.feed.generator,
            'language': parsed.feed.language
        }
        ch = Channel.objects.create(**data)
        return ch

    def parsed_to_model(self):
        return False