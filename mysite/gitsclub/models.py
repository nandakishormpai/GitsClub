from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=50) # Harikrishnan6336
    profilePic = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    starCount = models.IntegerField()
    repoCount = models.IntegerField()
    followerCount = models.IntegerField()
    contributionCount = models.IntegerField(default=0)
    
    def __str__(self):
        return self.userId
