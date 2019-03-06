from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^home/',views.photos_today,name='photosToday'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
