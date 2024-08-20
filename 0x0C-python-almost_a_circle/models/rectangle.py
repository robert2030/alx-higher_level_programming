#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, name, value):
        """Validate that a value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def validate_positive(self, name, value):
        """Validate that a value is positive (> 0)."""
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_non_negative(self, name, value):
        """Validate that a value is non-negative (>= 0)."""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle with '#' characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args, **kwargs):
        """Update attributes with arguments."""
        attr_names = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
