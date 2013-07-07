# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from views import book_list, push_book, new_url_access,\
src_addr_tail_check, add_book_from_file

urlpatterns = patterns('',
    (r'^aituidao/book_list/$', book_list),
    (r'^aituidao/push_book/$', push_book),
    (r'^aituidao/new_url_access/$', new_url_access),
    (r'^aituidao/src_addr_tail_check/$', src_addr_tail_check),
    # admit
    (r'^aituidao/admit/add_book_from_file/(.+)/$', add_book_from_file),
)
