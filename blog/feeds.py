from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.views import Feed
import models

class RSSFeed(Feed):
    title = "orn.li/blog"
    link = '/'
    description = "lol"

    def items(self):
        return models.Post.objects.order_by('-created')[:5]


class AtomFeed(RSSFeed):
    feed_type = Atom1Feed
    subtitle = RSSFeed.description
