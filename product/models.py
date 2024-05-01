from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='product_images/',null=True,blank=True)
    youtube_video_url = EmbedVideoField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.Product
    
    