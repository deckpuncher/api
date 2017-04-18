""" Basic jobseeker object and profile sub resource """
from django.db import models
from random import randint

# Create your models here.
class Jobseeker(models.Model):
    """ Basic information about a jobseeker """
    jobseeker_id = models.CharField(max_length=8, primary_key=True, default=randint(10000000, 99999999), name="JobseekerId")
    first_name = models.CharField(max_length=100, name="FirstName")
    last_name = models.CharField(max_length=100, name="LastName")
    email_address = models.CharField(max_length=200, name="Email")
    dob = models.DateField('DOB')

    def __str__(self):
        return  "{0} {1} {2}".format(self.JobseekerId, self.FirstName, self.LastName) # todo: figure out why the ide hates this

class Profile(models.Model):
    """ Jobseekers public facing profile """
    jobseeker = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=1000, name="AboutMe")
    preferred_work_location = models.CharField(max_length=50, name="PreferredWorkLocation")
    preferred_industry = models.CharField(max_length=200, name="PreferredIndustry")
    skills = models.CharField(max_length=50, name="Skills")

    def __str__(self):
        return "Profile for : {0} {1}".format(self.jobseeker.FirstName, self.jobseeker.LastName) # and this





