from django.db import models
from django.utils.timezone import now

class image(models.Model):
    id= models.AutoField(primary_key=True)
    title=models.CharField(max_length=101)
    slug=models.CharField(max_length=101, default=title)
    email=models.EmailField()
    salary=models.FloatField()
    details=models.TextField()
    available=models.BooleanField()
    created_at= models.DateTimeField(default=now())
    image=models.ImageField(default='default.jpg', upload_to='images')