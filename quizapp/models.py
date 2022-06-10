from django.db import models

# Create your models here.

class Questionpage(models.Model):
    questiontext=models.CharField(max_length=200,null=True)
    first=models.CharField(max_length=200,null=True)
    second=models.CharField(max_length=200,null=True)
    third=models.CharField(max_length=200,null=True)
    fourth=models.CharField(max_length=200,null=True)
    ans=models.CharField(max_length=200,null=True)

   