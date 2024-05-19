from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=(('IT','IT'),('Non IT', 'Non IT')))
    about = models.CharField(max_length=70)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length = 70)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    position = models.CharField(max_length=50, choices=(('manager','manager'),('leader','TL'),('software developer', 'SD')))

    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    
                            
