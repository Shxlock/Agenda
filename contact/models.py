from django.db import models
from datetime import date,datetime
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    company = models.CharField(max_length=20, blank=False, null=False)
    date_of_inclusion = models.DateField(default = date.today)
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name