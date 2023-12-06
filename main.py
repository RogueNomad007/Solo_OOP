import math


class Weight():
    def calculate_volume(self):
        pass
    def calculate_surface_area(self):
        pass
    def calculate_weight(self):
        pass

class Sphere_of_lead(Weight):
    def __init__(self, radius):
        self.radius = radius

    def calculate_volume(self):
        return (self.radius ** 3) * math.pi * (4 / 3)

    def calculate_surface_area(self):
        return (self.radius ** 2) * 4 * math.pi

    def calculate_weight(self):
        return 11343 * ((self.radius ** 3) * math.pi * (4 / 3))


class Sphere_of_aluminium(Weight):
    def __init__(self, radius):
        self.radius = radius

    def calculate_volume(self):
        return (self.radius ** 3) * math.pi * (4 / 3)

    def calculate_surface_area(self):
        return (self.radius ** 2) * 4 * math.pi

    def calculate_weight(self):
        return 2700 * ((self.radius ** 3) * math.pi * (4 / 3))


r = 1
lead_sphere = Sphere_of_lead(r)
lead_sphere_volume = Sphere_of_lead.calculate_volume(lead_sphere)
lead_sphere_surface_area = Sphere_of_lead.calculate_surface_area(lead_sphere)
lead_sphere_weight = Sphere_of_lead.calculate_weight(lead_sphere)
print(f"The lead sphere of radius {r} m has:")
print(f"a surface area of {lead_sphere_surface_area} meters squared.")
print(f"a volume of {lead_sphere_volume} meters cubed.")
print(f"a weight of {lead_sphere_weight} kilograms.")

print("\n")
r = 10
aluminium_sphere = Sphere_of_aluminium(r)
aluminium_sphere_volume = Sphere_of_aluminium.calculate_volume(aluminium_sphere)
aluminium_sphere_surface_area = Sphere_of_aluminium.calculate_surface_area(aluminium_sphere)
aluminium_sphere_weight = Sphere_of_aluminium.calculate_weight(aluminium_sphere)
print(f"The aluminium sphere of radius {r} m has:")
print(f"a surface area of {aluminium_sphere_surface_area} meters squared.")
print(f"a volume of {aluminium_sphere_volume} meters cubed.")
print(f"a weight of {aluminium_sphere_weight} kilograms.")