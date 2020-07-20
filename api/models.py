from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.CharField(max_length=100)


class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    branches = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')


class Contact(models.Model):
    CONTACTS_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Phone', 'Phone'),
        ('Email', 'Email'),
    ]
    type = models.CharField(max_length=15, choices=CONTACTS_CHOICES)
    contacts = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
    value = models.CharField(max_length=100)