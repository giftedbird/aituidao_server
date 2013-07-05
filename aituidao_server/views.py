#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json

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
    except Exception:
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
    except Exception:
        pass
    
    return HttpResponse(result)


def new_url_access(request):
    result = ur'{"status":-1}'
    
    try:
        responseStr = new_url_access_internal()
        if responseStr != None:
            result = responseStr 
    except Exception:
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
    except Exception:
        pass
    
    return HttpResponse(result)


# internal function
def book_list_internal(sortType, pageNo, count):
    return ur'{"bookList":[{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"阿丫","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146100086799.jpg","id":59,"intro":"本书是一本培养着装风格，提升个人品味的书。资深时装造型师阿丫以平实的视角，将看似复杂高深的穿衣之道回归简单，诠释了第一夫人风格、中产LADY风格、“白骨精”风格、文艺青年风格、摇滚GIRL风格等，35种时尚单品，28种混搭技巧，教你聪明搭衣，精明购衣。同时记录了自己的生活感悟、着装心得及一些时装品牌的风格，并在不经意间透露了当下时装行业的小秘密。浸润其中你会慢慢成长为褪去时装，依然FASHION的时尚ICON。","pushCount":41,"title":"人群中,你就是那个“例外”"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"阿丫","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146100086799.jpg","id":59,"intro":"本书是一本培养着装风格，提升个人品味的书。资深时装造型师阿丫以平实的视角，将看似复杂高深的穿衣之道回归简单，诠释了第一夫人风格、中产LADY风格、“白骨精”风格、文艺青年风格、摇滚GIRL风格等，35种时尚单品，28种混搭技巧，教你聪明搭衣，精明购衣。同时记录了自己的生活感悟、着装心得及一些时装品牌的风格，并在不经意间透露了当下时装行业的小秘密。浸润其中你会慢慢成长为褪去时装，依然FASHION的时尚ICON。","pushCount":41,"title":"人群中,你就是那个“例外”"},{"author":"阿丫","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146100086799.jpg","id":59,"intro":"本书是一本培养着装风格，提升个人品味的书。资深时装造型师阿丫以平实的视角，将看似复杂高深的穿衣之道回归简单，诠释了第一夫人风格、中产LADY风格、“白骨精”风格、文艺青年风格、摇滚GIRL风格等，35种时尚单品，28种混搭技巧，教你聪明搭衣，精明购衣。同时记录了自己的生活感悟、着装心得及一些时装品牌的风格，并在不经意间透露了当下时装行业的小秘密。浸润其中你会慢慢成长为褪去时装，依然FASHION的时尚ICON。","pushCount":41,"title":"人群中,你就是那个“例外”"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"小泉吉宏","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146121452693.jpg","id":52,"intro":"★ 经典中的经典！畅销1800万册，横扫亚洲的“小幸福神书”首次登陆中国内地！","pushCount":23,"title":"佛陀与想太多的猪1"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"阿丫","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146100086799.jpg","id":59,"intro":"本书是一本培养着装风格，提升个人品味的书。资深时装造型师阿丫以平实的视角，将看似复杂高深的穿衣之道回归简单，诠释了第一夫人风格、中产LADY风格、“白骨精”风格、文艺青年风格、摇滚GIRL风格等，35种时尚单品，28种混搭技巧，教你聪明搭衣，精明购衣。同时记录了自己的生活感悟、着装心得及一些时装品牌的风格，并在不经意间透露了当下时装行业的小秘密。浸润其中你会慢慢成长为褪去时装，依然FASHION的时尚ICON。","pushCount":41,"title":"人群中,你就是那个“例外”"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"小泉吉宏","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146121452693.jpg","id":52,"intro":"★ 经典中的经典！畅销1800万册，横扫亚洲的“小幸福神书”首次登陆中国内地！","pushCount":23,"title":"佛陀与想太多的猪1"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"小泉吉宏","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146121452693.jpg","id":52,"intro":"★ 经典中的经典！畅销1800万册，横扫亚洲的“小幸福神书”首次登陆中国内地！","pushCount":23,"title":"佛陀与想太多的猪1"},{"author":"（日）麻耶雄嵩 ","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130701/137266854547779.jpg","id":50,"intro":"新本格鬼才麻耶雄嵩力作！这个家伙还能写出“中规中矩”的推理？！不信的话，就请阅读这部《贵族侦探》。","pushCount":4,"title":"贵族侦探"},{"author":"小泉吉宏","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146121452693.jpg","id":52,"intro":"★ 经典中的经典！畅销1800万册，横扫亚洲的“小幸福神书”首次登陆中国内地！","pushCount":23,"title":"佛陀与想太多的猪1"},{"author":"小泉吉宏","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146121452693.jpg","id":52,"intro":"★ 经典中的经典！畅销1800万册，横扫亚洲的“小幸福神书”首次登陆中国内地！","pushCount":23,"title":"佛陀与想太多的猪1"},{"author":"阿丫","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146100086799.jpg","id":59,"intro":"本书是一本培养着装风格，提升个人品味的书。资深时装造型师阿丫以平实的视角，将看似复杂高深的穿衣之道回归简单，诠释了第一夫人风格、中产LADY风格、“白骨精”风格、文艺青年风格、摇滚GIRL风格等，35种时尚单品，28种混搭技巧，教你聪明搭衣，精明购衣。同时记录了自己的生活感悟、着装心得及一些时装品牌的风格，并在不经意间透露了当下时装行业的小秘密。浸润其中你会慢慢成长为褪去时装，依然FASHION的时尚ICON。","pushCount":41,"title":"人群中,你就是那个“例外”"},{"author":"小泉吉宏","coverUrl":"http://d31i1rfrna7v3n.cloudfront.net/image/20130617/137146121452693.jpg","id":52,"intro":"★ 经典中的经典！畅销1800万册，横扫亚洲的“小幸福神书”首次登陆中国内地！","pushCount":23,"title":"佛陀与想太多的猪1"}],"nextPageNum":1,"status":1}'


def push_book_internal(bookId, addr):
    return ur'{"status":1}'


def new_url_access_internal():
    return ur'{"status":1}'


def src_addr_tail_check_internal():
    return ur'{"status":1}'

