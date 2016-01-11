from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from riganinja.models import Item
from riganinja.rss_tools import RSSTools


class ItemResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'title': 'title',
        'link': 'link',
        'description': 'description',
        'author': 'author',
        'category': 'category',
        'pubDate': 'pubDate',
    })

    # GET /api/items/ (but not hooked up yet)
    def list(self):
        tools = RSSTools('ru')
        parsed = tools.get_parsed_results()
        tools.parsed_to_model(parsed)
        return Item.objects.all()

    # GET /api/items/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return Item.objects.get(id=pk)