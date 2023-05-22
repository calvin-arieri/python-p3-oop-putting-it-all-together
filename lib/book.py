#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def likesOfReader(self):
        print("i like reading", self.title, "It has" , self.page_count)
    
book = Book ("And Then There Were None", 272)
book.title
book.page_count



    
        