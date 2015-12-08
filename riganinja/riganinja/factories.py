import factory

from riganinja.models import Item, Channel


class ChannelFactory(factory.Factory):
    class Meta:
        model = Channel

    title = factory.Faker('word')
    description = factory.Faker('word')
    link = factory.Faker('url')
    lastBuildDate = factory.Faker('date_time')
    generator = factory.Faker('word')
    language = factory.Faker('word')


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
    channel_id = 1