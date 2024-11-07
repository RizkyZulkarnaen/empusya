from django.db import models

class DynamicField(models.Model):
    FIELD_TYPES = [
        ('char', 'Text'),
        ('int', 'Number'),
        ('email', 'Email'),
    ]
    
    name = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    field_type = models.CharField(max_length=10, choices=FIELD_TYPES)
    ecommerce_type = models.CharField(max_length=250)

    def __str__(self):
        return self.label
