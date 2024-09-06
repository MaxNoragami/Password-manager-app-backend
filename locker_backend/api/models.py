from django.db import models

# Create your models here.
class PasswordItem(models.Model):
    itemName = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'password-items'

    def __str__(self):
        return self.itemName