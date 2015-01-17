from django.contrib import admin

from .models import PressRelease, NewsItem, OtherContent

class ContentAdmin(admin.ModelAdmin):
	search_fields = ("old_id",)

admin.site.register(PressRelease, ContentAdmin)
admin.site.register(NewsItem, ContentAdmin)
admin.site.register(OtherContent, ContentAdmin)
