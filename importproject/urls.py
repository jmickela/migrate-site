from django.conf.urls import patterns, include, url
from django.contrib import admin

from content.views import NewsList, OtherContentList, PressList, ChemicalsList, ActionAlertList, ReportList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'importproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^action-alerts', ActionAlertList.as_view()),
    url(r'^reports', ReportList.as_view()),
    url(r'^chemicals', ChemicalsList.as_view()),
    url(r'^news-items', NewsList.as_view()),
    url(r'^other-content', OtherContentList.as_view()),
    url(r'^press-items', PressList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)