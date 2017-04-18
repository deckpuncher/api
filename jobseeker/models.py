""" Basic jobseeker object and profile sub resource """
from django.db import models

# Create your models here.
class Jobseeker(models.Model):
    """ Basic information about a jobseeker """
    first_name = models.CharField(max_length=100, name="FirstName")
    last_name = models.CharField(max_length=100, name="LastName")
    email_address = models.CharField(max_length=200, name="Email")
    dob = models.DateField('Date of Birth')

class Profile(models.Model):
    """ Jobseekers public facing profile """
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=1000, name="AboutMe")
    preferred_work_location = models.CharField(max_length=50, name="PreferredWorkLocation")
    preferred_industry = models.CharField(max_length=200, name="PreferredIndustry")
    skills = models.CharField(max_length=50, name="Skills")

    

