from django.contrib import admin
from .models import Product
from embed_video.admin import AdminVideoMixin


admin.site.register(Product)
