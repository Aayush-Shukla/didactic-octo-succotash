from django.db import models

# Create your models here.
class Search(models.Model):
    search=models.CharField(max_length=500, null=True)
    created=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return '{}'.format(self.search)