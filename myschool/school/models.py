from typing import Any
from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ValidationError

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=True)
    
    physics_Total_marks = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    chemistry_Total_marks = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    maths_Total_marks = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    physics_obtained_marks = models.PositiveIntegerField(default=1)
    chemistry_obtained_marks = models.PositiveIntegerField(default=1)
    maths_obtained_marks = models.PositiveIntegerField(default=1)

    def Check(self):
        if self.physics_Total_marks < self.physics_obtained_marks:
            raise ValueError("obtained marks must be smaller than total marks")
        
        if self.chemistry_Total_marks < self.chemistry_obtained_marks:
            raise ValueError("obtained marks must be smaller than total marks")

        if self.maths_Total_marks < self.maths_obtained_marks:
            raise ValueError("obtained marks must be smaller than total marks")
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Student, self).__init__(*args, **kwargs)
        self.Check()

    def __str__(self) -> str:
        return self.name

