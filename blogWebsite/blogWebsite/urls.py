"""blogWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
import xadmin

from django.conf import settings
from django.conf.urls.static import static

from blog.feed import LatestEntriesFeed

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry


info_dict={
	'queryset':Entry.objects.all(),
	'date_field':'modified_time'
}

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^blog/',include("blog.urls")),
    url(r'^latest/feed/$',LatestEntriesFeed()), #RSS订阅
    url(r'sitemap\.xml$',sitemap,{'sitemaps':{'blog':GenericSitemap(info_dict,priority=0.6)}},
    	name='django.contrib.sitemaps.views.sitemap'), #站点地图
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    #添加图片的url


