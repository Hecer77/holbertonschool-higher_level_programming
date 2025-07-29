#!/usr/bin/python3
"""
Bu modul Rectangle sinfini təyin edir.
Sinif genişlik və hündürlük atributları ilə obyekt yaradır
və bu atributların doğruluğunu setter-lərlə yoxlayır.
"""


class Rectangle:
    """Genişlik və hündürlüyə sahib düzbucaqlı sinfi"""

    def __init__(self, width=0, height=0):
        """Yeni düzbucaqlı obyektini yaradır"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Genişliyi qaytarır"""
        return self.__width

    @width.setter
    def width(self, value):
        """Genişliyi təyin edir, düzgünlüyü yoxlayır"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü qaytarır"""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir, düzgünlüyü yoxlayır"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def dict(self):
        """Obyektin atributlarını qaytarır"""
        return {"width": self.__width, "height": self.__height}
