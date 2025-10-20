class Circle:
    def area(self, radius):
        return 3.14 * radius * radius
    def perimeter(self, radius):
        return 2 * 3.14 * radius
r = float(input("Enter the radius: "))
c = Circle()
print("Area:", c.area(r))
print("Perimeter:", c.perimeter(r))
