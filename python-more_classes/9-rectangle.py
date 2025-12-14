#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """A class that defines a rectangle with square factory method."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height.

        Args:
            width: The width of the rectangle (must be integer >= 0).
            height: The height of the rectangle (must be integer >= 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value: The new width (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value: The new height (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle with print_symbol.

        Returns:
            String representation of rectangle, or empty string if size is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for i in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Return official string representation of the rectangle.

        Returns:
            String that can recreate the rectangle using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return the bigger one based on area.

        Args:
            rect_1: First rectangle (must be Rectangle instance).
            rect_2: Second rectangle (must be Rectangle instance).

        Returns:
            The rectangle with the bigger area, or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with equal width and height.

        Args:
            size: The size for both width and height.

        Returns:
            A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
EOFcat > 9-rectangle.py << 'EOF'
#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """A class that defines a rectangle with square factory method."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height.

        Args:
            width: The width of the rectangle (must be integer >= 0).
            height: The height of the rectangle (must be integer >= 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value: The new width (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value: The new height (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle with print_symbol.

        Returns:
            String representation of rectangle, or empty string if size is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for i in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Return official string representation of the rectangle.

        Returns:
            String that can recreate the rectangle using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return the bigger one based on area.

        Args:
            rect_1: First rectangle (must be Rectangle instance).
            rect_2: Second rectangle (must be Rectangle instance).

        Returns:
            The rectangle with the bigger area, or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with equal width and height.

        Args:
            size: The size for both width and height.

        Returns:
            A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
