# Generated by Django 3.1.1 on 2020-09-24 12:22

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
