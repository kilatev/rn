from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from riganinja.models import Item


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
        return Item.objects.all()

    # GET /api/items/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return Item.objects.get(id=pk)