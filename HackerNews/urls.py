from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HackerNews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r"", include('stories.urls'))
)
