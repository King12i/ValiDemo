from django.db import models

# Iport datetime object functionalities
from datetime import datetime

# Create your models here.
class VirusManager(models.Manager):
    def virus_validate(self, postData):
        errors = {}

        
        # Validation for minimum 3 characters in length
                        # v This is whatever the field in the html is named
        if len(postData['name']) < 3:
            errors['name_length'] = "Virus name must be at least 3 characters in length." #<-- This message is going to show up for the user on an invalid submission
        # Validation for making the name be fewer than 101 characters in length
        elif len(postData['name']) > 100:
            errors['name_length'] = "Virus name cannot exceed 100 characters in lenght."
        
        # Validation for uniqueness
        viruses = Viruses.objects.filter(name=postData['name'])
        if len(viruses) > 0:
            errors['name_taken'] = "Virus with that name already exists."

        # Checking to make sure that the incubation submitted isn't blank    
        if len(postData['incubation']) < 1:
            errors['incubation_time'] = "You must enter an incubation period."
        # Validation for an actual numerical incubation period longer than 0 days
        elif int(postData['incubation']) < 1:
            errors['incubation_time'] = "Virus must incubate for minimum 1 day."
        

        # WARNING, BE VERY CAREFUL WHEN USING TRY EXCEPTS
        try:
            # Validation for making sure discovered date is in the past
            if datetime.strptime(postData['discovered'], "%Y-%m-%d") > datetime.now():
                errors['discovered'] = "Stop messing with the spacetime continuum."
        except:
            errors['discovered'] = "Stop it you."    
        return errors


class Viruses(models.Model):
    name = models.CharField(max_length=100)
    incubation_period = models.IntegerField()
    discovered = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = VirusManager()

