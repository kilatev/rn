import factory

from riganinja.models import Item


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    title = factory.Faker('word')
    link = factory.Faker('url')
    guid = factory.Faker('ipv4')
    description = factory.Faker('text')
    author = factory.Faker('first_name')
    category = factory.Faker('word')
    pubDate = factory.Faker('date_time')
    channel = factory.Faker('word')