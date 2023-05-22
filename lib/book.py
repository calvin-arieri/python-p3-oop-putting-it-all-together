#!/usr/bin/env python3

class Book:
    def __init__(self, tittle, author, year ):
        self.tittle = tittle
        self.author = author
        self.year = year
    def likesOfReader(self):
        print("i like reading", self.tittle, "written by", self.author, "in the year", self.year)
    
article = Book ("A Doll's House", "Calvin Arieri", 1983)
article.likesOfReader()


    
        