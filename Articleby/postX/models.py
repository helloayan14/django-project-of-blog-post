from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=240)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)
   

    def __str__(self) -> str:
        return f'{self.user.username} - {self.text[:10]}'

