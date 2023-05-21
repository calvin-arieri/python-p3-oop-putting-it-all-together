#!/usr/bin/env python3

class Book:
    def __init__(self, title, name , rating):
        self.title =title
        self.name = name
        self.rating = rating
    def introduceBook(self):
        print(self.title, self.name, self.rating)
    def addBookRating(self):
        self.rating = int(self.rating) + 1
    def reduceRating(self):
        self.rating = int(self.rating) -1
        
class Author(Book):
    def __init__(self, title, name, rating,fname, lname):
        super().__init__(title, name, rating)
        self.fname =fname 
        self.lname = lname
    def introduceBookByAuthor(self):
        print(self.fname, self.lname, self.title, self.rating,self.name)

dollsHouse = Author("A doll's House", "Henrik Ibsen", "1", "Henrik", "Ibsen")
Author.introduceBook()


    
        