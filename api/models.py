from django.db import models
from django.contrib.auth.models import User

# Model to represent the original location (Lab or Classroom)
class Location(models.Model):
    LAB = 'Lab'
    CLASSROOM = 'Classroom'

    LOCATION_CHOICES = [
        (LAB, 'Lab'),
        (CLASSROOM, 'Classroom')
    ]

    name = models.CharField(max_length=100)
    location_type = models.CharField(
        max_length=10,
        choices=LOCATION_CHOICES,
        default=CLASSROOM
    )
    
    def __str__(self):
        return f'{self.name} ({self.get_location_type_display()})'


# Model to represent the type of goods (for example, electronic, furniture, etc.)
class GoodsType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


# Model to represent the goods themselves
class Goods(models.Model):
    code = models.CharField(max_length=50, unique=True)  # Unique identifier for goods
    description = models.TextField()
    keeper = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='goods')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='goods')
    type = models.ForeignKey(GoodsType, on_delete=models.CASCADE, related_name='goods')
    
    def __str__(self):
        return f'{self.code} - {self.type.name}'
    
    class Meta:
        # Indexing can be added to optimize the search for goods
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['keeper']),
            models.Index(fields=['location']),
        ]
