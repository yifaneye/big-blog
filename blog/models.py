from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class BlogIndexPage(Page):
    subtitle = models.TextField()
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body')
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    summary = models.TextField()
    body = RichTextField(blank=True)
