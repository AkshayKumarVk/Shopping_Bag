from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class productsDb(models.Model):
    productId = models.AutoField
    productCategory = models.CharField(default="", max_length=50)
    productBrands = models.CharField(default="", max_length=50)
    productDescription = models.TextField()
    productPrice = models.IntegerField(default=0)
    publishedDate = models.DateField(auto_now=False, auto_now_add=False)
    productImage = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.productDescription


# for delivery
class myOrderDb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Items_Json = models.CharField(max_length=5000, default="")
    First_Name = models.CharField(max_length=90)
    second_Name = models.CharField(max_length=90)
    Email = models.CharField(max_length=90)
    phone = models.IntegerField(default=0)
    Address1 = models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Pin_code = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Email


# for contact
class contactUsDb(models.Model):
    Name = models.CharField(max_length=90)
    Email = models.EmailField(max_length=90)
    Subject = models.CharField(max_length=90)
    Message = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Email


