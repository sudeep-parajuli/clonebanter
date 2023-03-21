from django.db import models

# Create your models here.
class CreateContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
