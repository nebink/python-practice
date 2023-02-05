import math

sphere_surface_area = lambda r: 4 * math.pi * r**2
sphere_volume = lambda r: (4/3) * math.pi * r**3

radius = float(input("Enter the radius of the sphere: "))
surface_area = sphere_surface_area(radius)
volume = sphere_volume(radius)

print("The surface area of the sphere is:", surface_area)
print("The volume of the sphere is:", volume)
