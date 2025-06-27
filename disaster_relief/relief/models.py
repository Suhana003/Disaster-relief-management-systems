from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Disaster(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
    
class Volunteer(models.Model):
    Fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    skills = models.TextField()

    def __str__(self):
        return self.Fullname


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    content = models.TextField()
    
    def __str__(self):
        return self.title
    


class MissingPerson(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender_choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    gender = models.CharField(max_length=10, choices=gender_choices)
    last_seen_location = models.CharField(max_length=255)
    date_last_seen = models.DateField()
    contact_info = models.CharField(max_length=255, help_text="Enter contact details of informant")
    # photo = models.ImageField(upload_to='missing_photos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Missing', 'Missing'), ('Found', 'Found')], default='Missing')
    photo = CloudinaryField('image', default="80e573ee1f1ef0fa0a70633ebfd74c54_a8xzti")  # Use your Cloudinary public ID

    def __str__(self):
        return f"{self.name} - {self.status}"
