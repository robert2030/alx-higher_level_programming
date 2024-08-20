#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update attributes of the square."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
