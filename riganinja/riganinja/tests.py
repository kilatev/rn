import factory

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from restless.constants import OK

from riganinja.models import Item
from riganinja.factories import ItemFactory


class ItemTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        items = ItemFactory.generate_batch(factory.CREATE_STRATEGY, 10)


    def test_list_items(self):
        url = reverse('api_item_list')
        resp = self.client.get(url)
        self.assertTrue(resp)
        self.assertEquals(resp.status_code, OK)
