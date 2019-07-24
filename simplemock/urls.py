from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),x
    url(r'^$', 'simplemock.core.views.home', name='home'),
    url(r'contato/', 'simplemock.core.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
