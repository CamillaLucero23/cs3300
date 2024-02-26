from django.db import models
from django.urls import reverse

class Portfolio(models.Model):

    title = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    about = models.CharField(max_length=400, blank=True)

    #Gets the name of the student and uses that for their display on /admin
    def __str__(self):
        return self.title
    
    #Gets URL to access instance of model
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('portfolio-detail', args=[str(self.id)])

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    #Gets the name of the student and uses that for their display on /admin
    def __str__(self):
        return self.title
    
    #Gets URL to access instance of model
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('project-detail', args=[str(self.id)])


class Student(models.Model):
#List of choices for major value in database, human readable name
    MAJOR = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )

    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200, choices=MAJOR, blank = True)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)

    #Gets the name of the student and uses that for their display on /admin
    def __str__(self):
        return self.name
    
    #Gets URL to access instance of model
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('student-detail', args=[str(self.id)])
    

