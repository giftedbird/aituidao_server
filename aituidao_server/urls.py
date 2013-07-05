from django.conf.urls import patterns, include, url
from views import book_list, push_book, new_url_access, src_addr_tail_check

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aituidao_server.views.home', name='home'),
    # url(r'^aituidao_server/', include('aituidao_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^book_list/$', book_list),
    ('^push_book/$', push_book),
    ('^new_url_access/$', new_url_access),
    ('^src_addr_tail_check/$', src_addr_tail_check),
)
