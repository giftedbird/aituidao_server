#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.db import transaction
import sys, os, json, random
from models import Book
from django.core.mail import send_mail

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
    except Exception, e:
        result = str(e)
    
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
    except Exception, e:
        result = str(e)
    
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

DEFAULT_UPLOAD_USER_NAME_MAP = (u"tangqi",
                                u"kong",
                                u"米兔",
                                u"小强强开看书",
                                u"eric",
                                )

EMAIL_SOURCE_ADDR_TAIL = "@aituidao.com"

def book_list_internal(sortType, pageNo, count):
    if sortType == SORT_TYPE_TIME:
        if pageNo < 0:
            books = Book.objects.order_by("-id")[:count + 1]
        else:
            books = Book.objects.filter(id__lte = pageNo).order_by("-id")[:count + 1]
        
        bookJsonList = [];
        for book in books[:count]:
            bookItem = {}
            bookItem["id"] = book.id
            bookItem["title"] = book.title
            bookItem["author"] = book.author
            bookItem["intro"] = book.intro
            bookItem["coverUrl"] = book.coverUrl
            bookItem["pushCount"] = book.pushCount
            bookItem["doubanRate"] = book.doubanRate
            bookItem["uploadUserName"] = DEFAULT_UPLOAD_USER_NAME_MAP[book.uploadUserId]
            
            bookJsonList.append(bookItem)
        
        if len(books) <= count:
            nextPageNum = -1;
        else:
            nextPageNum = books[count].id
        
        bookListJson = {}
        bookListJson["status"] = 1
        bookListJson["bookList"] = bookJsonList
        bookListJson["nextPageNum"] = nextPageNum
        
        return json.dumps(bookListJson)
    
    elif sortType == SORT_TYPE_HOT:
        if pageNo < 0:
            books = Book.objects.order_by("-pushCount", "-id")[:count + 1]
        else:
            books = Book.objects.filter(pushCount__lte = pageNo).order_by("-pushCount", "-id")[:count + 1]
        
        bookJsonList = [];
        for book in books[:count]:
            bookItem = {}
            bookItem["id"] = book.id
            bookItem["title"] = book.title
            bookItem["author"] = book.author
            bookItem["intro"] = book.intro
            bookItem["coverUrl"] = book.coverUrl
            bookItem["pushCount"] = book.pushCount
            bookItem["doubanRate"] = book.doubanRate
            bookItem["uploadUserName"] = DEFAULT_UPLOAD_USER_NAME_MAP[book.uploadUserId]
            
            bookJsonList.append(bookItem)
        
        if len(books) <= count:
            nextPageNum = -1;
        else:
            first =  books[count - 1].pushCount
            second = books[count].pushCount
            if first == second:
                nextPageNum = second - 1
            else:
                nextPageNum = second
        
        bookListJson = {}
        bookListJson["status"] = 1
        bookListJson["bookList"] = bookJsonList
        bookListJson["nextPageNum"] = nextPageNum
        
        return json.dumps(bookListJson)
    else:
        return None


def push_book_internal(bookId, addr):
    head = addr[0 : addr.index("@") + 1]
    book = Book.objects.filter(bookId = bookId)[0]
    
    send_mail(book.title, book.title, head + EMAIL_SOURCE_ADDR_TAIL,
    ['giftedbird@163.com'], fail_silently=False)
    
    
    
    
    
    
    
    return ur'{"status":1}'


def new_url_access_internal():
    return ur'{"status":1}'


def src_addr_tail_check_internal():
    return ur'{"status":1}'


@transaction.commit_on_success
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
            coverUrl = unicode(dataDict.get('coverUrl'))
            filename = unicode(dataDict['filename'])
            pushCount = int(dataDict.get('pushCount', 0))
            doubanRate = int(dataDict['doubanRate'])
        except:
            result = result + '<p><font color="#FF0000">json lose key error ---- ' + line + '</font></p>'
            continue
        
        if (cover != None) and (len(cover) != 0) and (not(os.path.exists(COVER_FILE_DICT + os.sep + cover))):
            result = result + '<p><font color="#FF0000">cover file error ---- ' + line + '</font></p>'
            continue
        
        if (coverUrl != None) and (not(coverUrl.startswith('http://'))) and (not(coverUrl.startswith('https://'))):
            result = result + '<p><font color="#FF0000">cover url format error ---- ' + line + '</font></p>'
            continue
        
        if not os.path.exists(BOOK_FILE_DICT + os.sep + filename):
            result = result + '<p><font color="#FF0000">database error ---- ' + line + '</font></p>'
            continue
        
        if pushCount < 0:
            pushCount = random.randint(5, 19)
        
        uploadUserId = random.randint(0, len(DEFAULT_UPLOAD_USER_NAME_MAP) - 1)
        
        try:
            book = Book(title = title, author = author, intro = intro,
                        cover = cover, coverUrl = coverUrl, filename = filename, pushCount = pushCount,
                        doubanRate = doubanRate, uploadUserId = uploadUserId)
            book.save()
        except:
            result = result + '<p><font color="#FF0000">database error ---- ' + line + '</font></p>'
            continue
        else:
            result = result + '<p><font color="33CC00">ok ---- ' + line + '</font></p>'
    
    result = result + '<p><font color="33CC00">Finish</font></p></body></html>'
    
    return result
