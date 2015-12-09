import factory
import json

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from restless.constants import OK

from riganinja.models import Item
from riganinja.factories import ItemFactory, ChannelFactory
from riganinja.rss_tools import RSSTools


class RSSToolsTestCase(TestCase):

    def setUp(self):
        self.rss_tools = RSSTools('ru')

    def test_get_feed_url(self):
        url = self.rss_tools.get_feed_url()
        self.assertTrue(url)
        self.assertEquals(url, 'https://www.riga.lv/rss/ru/news/')

    def test_get_parsed_results(self):
        self.assertTrue(self.rss_tools.get_parsed_results())

    def test_parsed_to_model(self):
        res = self.rss_tools.parsed_to_model()
        self.assertTrue(res)

    def test_create_channel(self):
        parsed = self.rss_tools.get_parsed_results()
        channel = self.rss_tools.create_channel(parsed)
        self.assertTrue(channel)


class ItemTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        channel = ChannelFactory()
        items = ItemFactory.generate_batch(factory.CREATE_STRATEGY, 10)
        channel.save()
        for item in items:
            item.channel.save()
            item.save()

    def test_list_items(self):
        url = reverse('api_item_list')
        resp = self.client.get(url)
        content =  json.loads(resp.content)
        self.assertTrue(resp)
        self.assertEquals(resp.status_code, OK)
        self.assertEquals(len(content['objects']), 10)
