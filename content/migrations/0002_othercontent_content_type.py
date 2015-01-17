# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='othercontent',
            name='content_type',
            field=models.IntegerField(default=1, verbose_name=b'Content Type', choices=[(1, b'Page'), (2, b'Chemical')]),
            preserve_default=True,
        ),
    ]
