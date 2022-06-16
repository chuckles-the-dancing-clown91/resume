from django.db import models

# Create your models here.


class Skills(models.Model):

    title = models.CharField(max_length=20, db_index=True)
    logo = models.ImageField(upload_to='logos')
    description = models.TextField()
    proficiency = models.FloatField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=60)
    number = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    position = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Employer(models.Model):

    name = models.CharField(max_length=110, db_index=True)
    logo = models.ImageField(upload_to='logos')
    skills_used = models.ManyToManyField(Skills)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    description = models.TextField()
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name