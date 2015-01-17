from django.db import models
from django.utils.text import slugify


PAGE = "page"
REPORT = "report"
NEWS = "news"
PRESS_RELEASE = "press-release"
ALERT = "alert"
RESOURCES = "resources"

TAXONOMY = (
	(PAGE, "Page"),
	(REPORT, "Report"),
	(NEWS, "News"),
	(PRESS_RELEASE, "Press Release"),
	(ALERT, "Alert"),
	(RESOURCES, "Resources")
)

class BaseContent(models.Model):
	old_id = models.IntegerField("Old ID")
	title = models.CharField("Title", max_length=255, blank=True)
	subtitle = models.CharField("Sub-Title", max_length=255, blank=True, null=True)
	body = models.TextField("Body", blank=True)
	summary = models.TextField("Summary", blank=True)
	date = models.DateField("Date", blank=True)
	datecreated = models.DateTimeField("Date Created", blank=True, null=True)

	new_url = models.CharField("New URL", max_length=255, blank=True, help_text="The URL this will be available at on the new site")
	author = models.CharField("Author", max_length=255, blank=True, null=True)
	updated = models.DateTimeField("Updated", null=True, blank=True)
	sourceurl = models.URLField("Source URL", null=True, blank=True)

	publish = models.IntegerField("Published?", null=True, blank=True)

	linktext = models.CharField("Link Text", max_length=256, blank=True, null=True)
	link = models.URLField("Link", blank=True, null=True)

	docname = models.CharField("Document Name", max_length=256, blank=True, null=True)
	picture = models.CharField("Picture File Name", max_length=256, blank=True, null=True)

	source = models.CharField("Source", max_length=256, blank=True, null=True)
	contact = models.CharField("Contact", max_length=256, blank=True, null=True)

	media = models.TextField("Media", blank=True, null=True)
	media_thumb_url = models.URLField("Media Thumb URL", blank=True, null=True)

	old_type = models.IntegerField("Old Type", help_text="Content Type on old site", blank=True, null=True)

	def get_new_url(self):
		if self.new_url is not None and self.new_url != "":
			return self.new_url
		else:
			return "NO_URL_SET"

	def __unicode__(self):
		if self.title is not None and self.title != "":
			return self.title
		elif self.subtitle is not None and self.subtitle != "":
			return self.subtitle
		else:
			return "No title specified"


class NewsItem(BaseContent):
	taxonomy = models.CharField("Taxonomy", default=NEWS, choices=TAXONOMY, blank=True, null=True, max_length=32)

	def get_new_url(self):
		return "/news/%s" % slugify(self.title)


class PressRelease(BaseContent):
	taxonomy = models.CharField("Taxonomy", default=PRESS_RELEASE, choices=TAXONOMY, blank=True, null=True, max_length=32)

	def get_new_url(self):
		return "/press-release/%s" % slugify(self.title)




class OtherContent(BaseContent):
	PAGE = 1
	CHEMICAL = 2
	ACTION_ALERT = 3
	REPORT = 4
	CONTENT_TYPES = (
		(PAGE, "Page"),
		(CHEMICAL, "Chemical"),
		(ACTION_ALERT, "Action Alert"),
		(REPORT, "Report")
	)

	content_type = models.IntegerField("Content Type", choices=CONTENT_TYPES, default=PAGE)
	taxonomy = models.CharField("Taxonomy", choices=TAXONOMY, blank=True, null=True, max_length=32)
	do_import = models.BooleanField("Import?", help_text="If left unchecked this item will not be imported.", default=False)





