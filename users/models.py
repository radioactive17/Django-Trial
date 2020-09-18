from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EndUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to = 'users/upload/')
    uid = models.CharField(max_length = 6)

    def __str__(self):
        return self.user
