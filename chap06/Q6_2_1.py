import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def calculate_volume(self):
        return math.pi * self.radius ** 2 * self.height

my_cylinder = Cylinder(radius=3, height=5)

surface_area = my_cylinder.calculate_surface_area()
volume = my_cylinder.calculate_volume()

print(f"円柱の半径: {my_cylinder.radius}")
print(f"円柱の高さ: {my_cylinder.height}")
print(f"円柱の表面積: {surface_area:.2f}")
print(f"円柱の体積: {volume:.2f}")

