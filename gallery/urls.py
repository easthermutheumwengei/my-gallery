from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import galleryView, detailsView, image_location
urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'location/(?P<location_name>\w+)/', views.image_location, name='location'),
    url(r'category/(?P<category>\w+)/', views.image_category, name='category'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'gallery/', galleryView.as_view(), name = 'gallery'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
