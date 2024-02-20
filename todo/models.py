from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=60, blank=False,null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)

    def clean(self):
        if int(self.priority) > 5:
            raise ValidationError("Solo se permite una prioridad maxima de 5 estrellas")
        if self.estimated_end < self.date:
            raise ValidationError("La fecha de terminacion no puede ser menor a la de inicio")

    def __str__(self):
        return self.title