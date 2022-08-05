from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    admin = models.BooleanField()
    adminView = models.CharField(max_length=7)

    def __str__(self):
        return self.first_name