# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_id', models.IntegerField(verbose_name=b'Old ID')),
                ('title', models.CharField(max_length=255, verbose_name=b'Title', blank=True)),
                ('subtitle', models.CharField(max_length=255, null=True, verbose_name=b'Sub-Title', blank=True)),
                ('body', models.TextField(verbose_name=b'Body', blank=True)),
                ('summary', models.TextField(verbose_name=b'Summary', blank=True)),
                ('date', models.DateField(verbose_name=b'Date', blank=True)),
                ('datecreated', models.DateTimeField(null=True, verbose_name=b'Date Created', blank=True)),
                ('new_url', models.URLField(help_text=b'The URL this will be available at on the new site', verbose_name=b'New URL', blank=True)),
                ('author', models.CharField(max_length=255, null=True, verbose_name=b'Author', blank=True)),
                ('updated', models.DateTimeField(null=True, verbose_name=b'Updated', blank=True)),
                ('sourceurl', models.URLField(null=True, verbose_name=b'Source URL', blank=True)),
                ('publish', models.IntegerField(null=True, verbose_name=b'Published?', blank=True)),
                ('linktext', models.CharField(max_length=256, null=True, verbose_name=b'Link Text', blank=True)),
                ('link', models.URLField(null=True, verbose_name=b'Link', blank=True)),
                ('docname', models.CharField(max_length=256, null=True, verbose_name=b'Document Name', blank=True)),
                ('picture', models.CharField(max_length=256, null=True, verbose_name=b'Picture File Name', blank=True)),
                ('source', models.CharField(max_length=256, null=True, verbose_name=b'Source', blank=True)),
                ('contact', models.CharField(max_length=256, null=True, verbose_name=b'Contact', blank=True)),
                ('media', models.TextField(null=True, verbose_name=b'Media', blank=True)),
                ('media_thumb_url', models.URLField(null=True, verbose_name=b'Media Thumb URL', blank=True)),
                ('old_type', models.IntegerField(help_text=b'Content Type on old site', null=True, verbose_name=b'Old Type', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('basecontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.BaseContent')),
                ('taxonomy', models.CharField(default=b'news', choices=[(b'page', b'Page'), (b'report', b'Report'), (b'news', b'News'), (b'press-release', b'Press Release'), (b'alert', b'Alert'), (b'resources', b'Resources')], max_length=32, blank=True, null=True, verbose_name=b'Taxonomy')),
            ],
            options={
            },
            bases=('content.basecontent',),
        ),
        migrations.CreateModel(
            name='OtherContent',
            fields=[
                ('basecontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.BaseContent')),
                ('taxonomy', models.CharField(blank=True, max_length=32, null=True, verbose_name=b'Taxonomy', choices=[(b'page', b'Page'), (b'report', b'Report'), (b'news', b'News'), (b'press-release', b'Press Release'), (b'alert', b'Alert'), (b'resources', b'Resources')])),
                ('do_import', models.BooleanField(default=False, help_text=b'If left unchecked this item will not be imported.', verbose_name=b'Import?')),
            ],
            options={
            },
            bases=('content.basecontent',),
        ),
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('basecontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.BaseContent')),
                ('taxonomy', models.CharField(default=b'press-release', choices=[(b'page', b'Page'), (b'report', b'Report'), (b'news', b'News'), (b'press-release', b'Press Release'), (b'alert', b'Alert'), (b'resources', b'Resources')], max_length=32, blank=True, null=True, verbose_name=b'Taxonomy')),
            ],
            options={
            },
            bases=('content.basecontent',),
        ),
    ]
