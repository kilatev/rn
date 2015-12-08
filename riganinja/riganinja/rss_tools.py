from django.conf import settings

from feedreader.parser import from_url


class RSSTools(object):

    def __init__(self, lang):
        self.lang = lang

    def get_feed_url(self):
        return settings.RSS_URLS[self.lang]

    def get_parsed_results(self):
        feed_url = self.get_feed_url()
        parsed = from_url(feed_url)
        print parsed.entries[0].link
        return parsed