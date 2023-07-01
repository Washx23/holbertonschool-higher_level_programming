#!/usr/bin/pyhton3
"""document"""

from models.base import Base

class rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
