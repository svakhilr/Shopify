from django.db import models
from django.urls import reverse
from django.utils import timezone
from account.models import Account

class Category(models.Model):
    category_name =  models.CharField(max_length=50, unique=True)
    slug          =  models.SlugField(max_length=50, unique=True)
    description   =  models.TextField(max_length=200 , blank=True)
    cat_img       =  models.ImageField(upload_to='catog_img')



    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('products_by_category' , args=[self.slug])

    
    class Meta:
        verbose_name='catagory'
        verbose_name_plural='catagories'


class Product(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    slug= models.SlugField(max_length=50,unique=True)
    price=models.IntegerField()
    description=models.TextField(max_length=500,blank=True)
    images = models.ImageField(upload_to="photos/products", null=True)
    images1 = models.ImageField(upload_to="photos/products", null=True)
    images2 = models.ImageField(upload_to="photos/products", null=True)
    images3 = models.ImageField(upload_to="photos/products", null=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )  # when delete a category all products related to that category will be deleted
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse("product-detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
    



class VariationManager(models.Manager):
    

    def size(self):
        return super(VariationManager,self).filter(variation_catogory='size', is_active=True)



variation_category_choice = (("size", "size"),)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variation')
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice
    )
    variation_value = models.CharField(max_length=7)
    
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)

    objects= VariationManager()

    

    def __str__(self):
        return str(self.variation_value)


class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)

