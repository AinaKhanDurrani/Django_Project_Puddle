from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    
    class Meta:
        ordering=['name',]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    description=models.TextField(blank=True, null=True)   
    price=models.DecimalField(max_digits=10, decimal_places=2)
    is_sold=models.BooleanField(default=False) 
    image=models.ImageField(upload_to='items_images' ,blank=True,null=True)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.name