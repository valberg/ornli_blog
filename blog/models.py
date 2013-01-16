from django.db import models
from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel
from django.core.urlresolvers import reverse

class Post(TimeStampedModel):
    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(max_length=50, blank=True)

    content = MarkupField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})
