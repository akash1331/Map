from django.db import models

# Create your models here.

class search(models.Model):
    address = models.CharField(max_length=20,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Search'