# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from views import book_list, push_book, new_url_access,\
src_addr_tail_check, add_book_from_file
from personal_setting import URL_BOOK_LIST_PATH_PATTERN,\
URL_PUSH_BOOK_PATH_PATTERN, URL_NEW_URL_ACCESS_PATH_PATTERN,\
URL_SRC_ADDR_TAIL_CHECK_PATH_PATTERN, URL_ADD_BOOK_FROM_FILE_PATH_PATTERN

urlpatterns = patterns('',
    (URL_BOOK_LIST_PATH_PATTERN, book_list),
    (URL_PUSH_BOOK_PATH_PATTERN, push_book),
    (URL_NEW_URL_ACCESS_PATH_PATTERN, new_url_access),
    (URL_SRC_ADDR_TAIL_CHECK_PATH_PATTERN, src_addr_tail_check),
    (URL_ADD_BOOK_FROM_FILE_PATH_PATTERN, add_book_from_file),
)
