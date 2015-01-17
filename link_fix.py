__author__ = 'Jason'
import re

import django
django.setup()

from django.db import connections
from django.db.utils import ConnectionDoesNotExist

from content.models import NewsItem, PressRelease, OtherContent, BaseContent

OLD_ID = 0
TITLE = 1
SUB_TITLE=2
BODY = 3
AUTHOR = 4
UPDATED = 5
TYPE = 6

PUBLISH = 8
LINKTEXT = 9
DOC=16
LINK=20
SUMMARY=22
DATE = 23
PICTURE = 28
SOURCE = 34
CONTACT = 35
CREATED = 40
SOURCEURL = 42
MEDIA_HTML = 57
MEDIA_THUMB = 59

search_for_links = re.compile("article\.php\?id\=\d+")
search_link_for_id = re.compile("\d+")

def fix_links(queryset):
	for item in queryset:
		print item.id
		links = search_for_links.findall(item.body)
		print links
		for link in links:
			ids = search_link_for_id.findall(link)
			linked_item = None
			for id in ids:
				try:
					linked_item = NewsItem.objects.get(old_id=id)
				except:
					pass
				try:
					linked_item = PressRelease.objects.get(old_id=id)
				except:
					pass
				try:
					linked_item = OtherContent.objects.get(old_id=id)
				except:
					pass
			item.body = item.body.replace("http://www.safecosmetics.org/", "")
			item.body = item.body.replace("http://safecosmetics.org/", "")
			if linked_item is not None:
				print link
				print linked_item
				item.body = item.body.replace("http://www.safecosmetics.org/", "")
				item.body = item.body.replace("http://safecosmetics.org/", "")
				item.body = item.body.replace(link, linked_item.get_new_url())
			else:
				item.body = item.body.replace(link, "/NOT_FOUND")

		item.save()

news_items = NewsItem.objects.filter(body__contains="article.php?id=")
press_items = PressRelease.objects.filter(body__contains="article.php?id=")
other_content = OtherContent.objects.filter(body__contains="article.php?id=")


fix_links(news_items)
fix_links(press_items)
fix_links(other_content)


