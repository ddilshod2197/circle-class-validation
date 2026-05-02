class Circle:
    def __init__(self, radius):
        self.radius = self._validate_radius(radius)

    @staticmethod
    def _validate_radius(radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        return radius

    def get_radius(self):
        return self.radius

# Test
try:
    circle = Circle(-5)
except ValueError as e:
    print(e)

circle = Circle(5)
print(circle.get_radius())
```

Kodda Circle klassi yaratilib, radiusni validatsiya qiluvchi _validate_radius metodining yordamida radiusni tekshirish uchun static metod ishlatilgan. Agar radius manfiy yoki 0 bo'lsa, ValueError istisno tashlanadi. Boshqa holatlarda radius saqlanib qoladi.
