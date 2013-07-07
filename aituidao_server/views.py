#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
import sys, os, json
from models import Book

def book_list(request):
    result = ur'{"status":-1}'
    
    try:
        postStr = request.POST['data']
        postDict = json.loads(postStr)
        
        sortType = int(postDict["sortType"])
        pageNo = long(postDict["pageNo"])
        count = int(postDict["count"])
        
        responseStr = book_list_internal(sortType, pageNo, count)
        if responseStr != None:
            result = responseStr 
    except:
        pass
    
    return HttpResponse(result)


def push_book(request):
    result = ur'{"status":-1}'
    
    try:
        postStr = request.POST['data']
        postDict = json.loads(postStr)
        
        bookId = long(postDict["id"])
        addr = str(postDict["addr"])
        
        responseStr = push_book_internal(bookId, addr)
        if responseStr != None:
            result = responseStr 
    except:
        pass
    
    return HttpResponse(result)


def new_url_access(request):
    result = ur'{"status":-1}'
    
    try:
        responseStr = new_url_access_internal()
        if responseStr != None:
            result = responseStr 
    except:
        pass
    
    return HttpResponse(result)


def src_addr_tail_check(request):
    result = ur'{"status":-1}'
    
    try:
        postStr = request.POST['data']
        postDict = json.loads(postStr)
        
        currTail = str(postDict["currTail"])
        
        responseStr = src_addr_tail_check_internal(currTail)
        if responseStr != None:
            result = responseStr 
    except:
        pass
    
    return HttpResponse(result)

def add_book_from_file(request, fileName):
    result = ur'{"status":-1}'
    
    try:
        responseStr = add_book_from_file_internal(fileName)
        if responseStr != None:
            result = responseStr 
    except:
        pass
    
    return HttpResponse(result)


# internal function
SORT_TYPE_TIME = 1
SORT_TYPE_HOT = 2

if sys.platform.startswith('darwin'):
    DICT_RELATIVE_TO_DB = r'/Users/yuanzhe/projects/files/aituidao/db_update'
elif sys.platform.startswith('win'):
    DICT_RELATIVE_TO_DB = r'E:\projects\files\aituidao\db_update'
else:
    DICT_RELATIVE_TO_DB = r'/home/giftedbird/projects/files/aituidao/db_update'

if sys.platform.startswith('darwin'):
    BOOK_FILE_DICT = r'/Users/yuanzhe/projects/files/aituidao/book_file'
elif sys.platform.startswith('win'):
    BOOK_FILE_DICT = r'E:\projects\files\aituidao\book_file'
else:
    BOOK_FILE_DICT = r'/home/giftedbird/projects/files/aituidao/book_file'

if sys.platform.startswith('darwin'):
    COVER_FILE_DICT = r'/Users/yuanzhe/projects/files/aituidao/book_cover_file'
elif sys.platform.startswith('win'):
    COVER_FILE_DICT = r'E:\projects\files\aituidao\book_cover_file'
else:
    COVER_FILE_DICT = r'/home/giftedbird/projects/files/aituidao/book_cover_file'


def book_list_internal(sortType, pageNo, count):
    if sortType == SORT_TYPE_TIME:
        #  需要重新写
        books = Book.objects.all();
        
        bookJsonList = [];
        for book in books:
            bookItem = {}
            bookItem["id"] = book.id
            bookItem["title"] = book.title
            bookItem["author"] = book.author
            bookItem["intro"] = book.intro
            bookItem["coverUrl"] = book.cover
            bookItem["pushCount"] = book.pushCount
            
            bookJsonList.append(bookItem)
        
        bookListJson = {}
        bookListJson["status"] = 1
        bookListJson["bookList"] = bookJsonList
        bookListJson["nextPageNum"] = 1
        
        return json.dumps(bookListJson)
    elif sortType == SORT_TYPE_HOT:
        #  需要重新写
        books = Book.objects.all();
        
        bookJsonList = [];
        for book in books:
            bookItem = {}
            bookItem["id"] = book.id
            bookItem["title"] = book.title
            bookItem["author"] = book.author
            bookItem["intro"] = book.intro
            bookItem["coverUrl"] = book.cover
            bookItem["pushCount"] = book.pushCount
            
            bookJsonList.append(bookItem)
        
        bookListJson = {}
        bookListJson["status"] = 1
        bookListJson["bookList"] = bookJsonList
        bookListJson["nextPageNum"] = 1
        
        return json.dumps(bookListJson)
    else:
        return None

def push_book_internal(bookId, addr):
    return ur'{"status":1}'


def new_url_access_internal():
    return ur'{"status":1}'


def src_addr_tail_check_internal():
    return ur'{"status":1}'

def add_book_from_file_internal(fileName):
    try:
        filePath = DICT_RELATIVE_TO_DB + os.sep + fileName
        f = open(filePath, 'r')
    except:
        return '<html><body><p><font color="#FF0000">file open error</font></p></body></html>'
    
    result = '<html><body>'
    
    for line in f:
        if line.startswith("#") or len(line.split()) == 0:
            continue
        
        try:
            dataDict = json.loads(line, 'utf-8')
        except:
            result = result + '<p><font color="#FF0000">json format error ---- ' + line + '</font></p>'
            continue
        
        try:
            title = unicode(dataDict['title'])
            author = unicode(dataDict['author'])
            intro = unicode(dataDict.get('intro'))
            cover = unicode(dataDict.get('cover'))
            filename = unicode(dataDict['filename'])
            pushCount = int(dataDict.get('pushCount', 0))
            doubanRate = int(dataDict['doubanRate'])
            deleted = False
        except:
            result = result + '<p><font color="#FF0000">json lose key error ---- ' + line + '</font></p>'
            continue
        
        if (cover != None) and (len(cover) != 0) and (not(os.path.exists(COVER_FILE_DICT + os.sep + cover))):
            result = result + '<p><font color="#FF0000">cover file error ---- ' + line + '</font></p>'
            continue
        
        if not os.path.exists(BOOK_FILE_DICT + os.sep + filename):
            result = result + '<p><font color="#FF0000">database error ---- ' + line + '</font></p>'
            continue
        
        try:
            book = Book(title = title, author = author, intro = intro,
                        cover = cover, filename = filename, pushCount = pushCount,
                        doubanRate = doubanRate, deleted = deleted)
            book.save()
        except:
            result = result + '<p><font color="#FF0000">database error ---- ' + line + '</font></p>'
            continue
        else:
            result = result + '<p><font color="33CC00">ok ---- ' + line + '</font></p>'
    
    result = result + '<p><font color="33CC00">Finish</font></p></body></html>'
    
    return result
