from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    Dep_Choices = (
        ('IT', 'Information Technology'),
        ('ME', 'Mechanical'),
        ('EE', 'Electrical'),
    )
    Year_Choices = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    roll = models.IntegerField()
    department = models.CharField(max_length=50, choices=Dep_Choices)
    year = models.CharField(max_length=3, choices=Year_Choices)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
