#!/usr/bin/python3

"""
This is module with class square that inherits from Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    this repr square, a special case with equal width and height.
    
    inherits from rectangle class

    Attr:
        Inherited from Rectangle.
        id (int): unique identifier of square.
        width(int): width of square.
        height (int): height of square.
        x (int): x cordinate of square's position.
        y (int): y cordinate of square's position.
    
    """
    
    def __init__(self, size, x=0, y=0, id=1):
        """
        This is class constructor that initialise square class

        Args:
            size (int): size of square equa to width and height.
            id (int, optional): unique identifier of square.
            x (int, optional): x cordinate of square's position.
            y (int, optional): y cordinate of square's position.

        """
        super().__init__(size, size, x, y, id=1)
        self.x = x
        self.y = y
        self.id = id

    def update(self, *args, **kwargs):
        """this function updates attributes of the rectangle

        Arguments:
        *args: Positional args to assign to the attr.

        Args should be in following order:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
            

        **kwargs can be thought of as a double pointer to a dictionary: key/value
            As Python doesn’t have pointers, **kwargs is not literally a double pointer –
            describing it as such is just a way of explaining its behavior in terms you’re
            already familiar with
        
        **kwargs must be skipped if *args exists and is not empty
        
        Each key in this dictionary represents an attribute to the instance

        The attr can be any combo of id, size, x, y

        """

        if len(args) > 0:
            if len(args) >= 1:    
                self.id = args[0]
            elif len(args) >= 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.size = args[1]
            else:
                raise ValueError("Invalid number of arguments.")
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            elif 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
                self.size = kwargs['size']
            elif 'x' in kwargs:
                self.x = kwargs['x']
            elif 'y' in kwargs:
                self.y = kwargs['y']


    def to_csv_row(self):
        """
        converts sq instance into csv ro.

        Returns:
            list: list repr sq nst attributes.

        """
        return [self.id, self.size, self.x, self.y]
    @property
    def size(self):
        """
        
        width getter
        
        Returns:
            int: Size of square.
            
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        
        setter of width and height
        
        Args:
            size (int): Size to be set for square.
            
        Raises:
            ValueError: if value is not positive int.
            
        """
        if not isinstance(size, int) or size <= 0:
            raise TypeError("width must be an integer.")
        
        self.width = size
        self.height = size

    

    def __str__(self):
        """Update the class Square by overriding the __str__ method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    
    def to_dictionary(self):
        """
        Returns dict repr of square.
        
        Returns:
            dict: Dict repr of square.
            
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
