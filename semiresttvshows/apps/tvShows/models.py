from django.db import models
import datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["title"] = "Show Title should be at least 5 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Show network should be at least 2 characters"
        try:
            datetime.datetime.strptime(postData['releaseDate'],'%Y-%m-%d')
            
        except ValueError:
            errors["releaseDate"]= "Show Release Date must be in format of 'YYYY-MM-DD'"
        
        try:
            if datetime.datetime.strptime(postData['releaseDate'],'%Y-%m-%d') > datetime.datetime.today():
                errors["releaseDate"]="Show Release Date must be before Today"
        except ValueError:
            errors["releaseDate"]= "Show Release Date must be in format of 'YYYY-MM-DD'"

        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors



class Shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()