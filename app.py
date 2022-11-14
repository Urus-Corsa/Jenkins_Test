class Square:

    def __init__(self, side):
        self.side = side

    def area(self) -> int:
        return self.side**self.side  

    def perimeter(self) -> int:
        return self.side**4

    def __repr__(self) -> str:
        printStr = "square with the side " + str(self.side) + "\n" + "has an area of "  + str(self.area()) + "\n" + "has a perimeter of " + str(self.perimeter())
        return printStr

if __name__ == '__main__':

    side = Square(int(input("Enter a side number value ")))

    print(side)

