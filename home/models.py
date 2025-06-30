from django.db import models

class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.last_name


class StudentsAbout(models.Model):
    username = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    image = models.ImageField(upload_to="students_about/",null=True, blank=True)
    body = models.TextField()
    def __str__(self):
        return self.username