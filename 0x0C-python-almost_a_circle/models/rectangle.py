#!/usr/bin/python3

"""
This is module with class Rectangle that inherits from Base
"""

from models.base import Base

class Rectangle(Base):
    """
    This is rectangle class that inherits from Base
    
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is class constructor that initialise rectangle class
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
    @property
    def width(self):
        """width getter"""
        return self.__width
    
    @property
    def height(self):
        """height getter"""
        return self.__height
    
    @property
    def x(self):
        """x getter"""
        return self.__x
    
    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, num):
        """setter of width"""
        if type(num) is not int:
            raise TypeError("width must be an integer")
        if num <= 0:
            raise ValueError("width must be > 0")
        self.__width = num

    @height.setter
    def height(self, num):
        """setter of height"""
        if type(num) is not int:
            raise TypeError("height must be an integer")
        if num <= 0:
            raise ValueError("height must be > 0")
        self.__height = num

    @x.setter
    def x(self, num):
        """setter of x"""
        if type(num) is not int:
            raise TypeError("x must be an integer")
        """if num <= 0:
            raise ValueError("x must be > 0")"""
        self.__x = num

    @y.setter
    def y(self, num):
        """setter of y"""
        if type(num) is not int:
            raise TypeError("y must be an integer")
        """if num <= 0:
            raise ValueError("y must be > 0")"""
        self.__y = num

    def area(self):
        """formulates area of a rectangle"""
        return self.__height * self.__width
    

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def to_csv_row(self):
        """
        converts rectangle instance into csv ro.

        Returns:
            list: list repr sq nst attributes.

        """
        return [self.id, self.width, self.height, self.x, self.y]

    def update(self, *args, **kwargs):
        """this function updates attributes of the rectangle

        Arguments:
        *args: Positional args to assign to the attr.

        Args should be in following order:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        **kwargs can be thought of as a double pointer to a dictionary: key/value
            As Python doesn’t have pointers, **kwargs is not literally a double pointer –
            describing it as such is just a way of explaining its behavior in terms you’re
            already familiar with
        
        **kwargs must be skipped if *args exists and is not empty
        
        Each key in this dictionary represents an attribute to the instance

        The attr can be any combo of id, width, height, x, y

        """

        if len(args):
            for index, a in enumerate(args):
                if index == 0:
                    self.id = a
                elif index == 1:
                    self.width = a
                elif index == 2:
                    self.height = a
                elif index == 3:
                    self.x = a
                elif index == 4:
                    self.y = a
        
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            elif 'width' in kwargs:
                self.width = kwargs['width']
            elif 'height' in kwargs:
                self.height = kwargs['height']
            elif 'x' in kwargs:
                self.x = kwargs['x']
            elif 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns dict repr of rectangle.
        
        Returns:
            dict: Dict repr of rectangle.
            
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
