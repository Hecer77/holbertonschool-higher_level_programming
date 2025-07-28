#!/usr/bin/python3
"""
Bu modul Rectangle sinfini təyin edir.
Sinif düzbucaqlı obyektləri genişlik və hündürlük ilə yaradır.
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.dict_ = {'width': self.width, 'height': self.height}
