#coding=utf-8
import urllib.request
import json
import string
from urllib.parse import quote


class BookSearcher_douban:
    def __init__(self,book_name):
        self.__book_name = book_name
    
    def __GetBookID(self):
        url = 'https://api.douban.com/v2/book/search?q=' + self.__book_name + '&fields=id,title'
        self.__s = quote(url,safe=string.printable)

        html = urllib.request.urlopen(self.__s)
        hjson = json.loads(html.read()) 
        book_id = hjson['books'][0]['id']
        return book_id

    def __GetBookInfo(self):
        url = 'https://api.douban.com/v2/book/' + self.__book_id
        self.__s = quote(url,safe=string.printable)
        html = urllib.request.urlopen(self.__s)
        hjson = json.loads(html.read())
        # print(hjson)
        self.__book_author = hjson['author']
        self.__book_catalog = hjson['catalog']
        self.__book_translator = hjson['translator']
        self.__book_price = hjson['price']
        self.__book_publisher = hjson['publisher']

    def MyInit(self):
        self.__book_id = self.__GetBookID()
        self.__GetBookInfo()

        self.book_id = self.__book_id
        self.book_author = self.__book_author
        self.book_catalog = self.__book_catalog
        self.book_translator = self.__book_translator
        self.book_price = self.__book_price
        self.book_publisher = self.__book_publisher
    
    def print_test(self):
        print(self.book_id)
        print(self.book_author)
        print(self.book_catalog)
        print(self.book_translator)
        print(self.book_price)
        print(self.book_publisher)


def main():
    book = input()
    a = BookSearcher_douban(book)
    a.MyInit()
    a.print_test()

if __name__ == '__main__':
    main()



