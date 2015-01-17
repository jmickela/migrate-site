# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_othercontent_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecontent',
            name='new_url',
            field=models.CharField(help_text=b'The URL this will be available at on the new site', max_length=255, verbose_name=b'New URL', blank=True),
            preserve_default=True,
        ),
    ]
