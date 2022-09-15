from django.db import models

# Create your models here.
class Staff(models.Model): #'id','fullname','department'
    
    category = [
        ('frozen food','frozen food'),
        ('fresh food','fresh food')
        
    ]
    fullname = models.CharField(max_length=50,verbose_name="Full Name")
    department = models.CharField(max_length=50,choices=category,verbose_name="Department")
    
    def __str__(self):
        return self.fullname+" "+self.department

class Customers(models.Model): #('fname','lname','email','categories')
    fname = models.CharField(max_length=50,null=False,verbose_name='First Name')
    lname = models.CharField(max_length=50,null=False,verbose_name='Last Name')
    email = models.EmailField(max_length=50,null=False,verbose_name="Email")
    categories = models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.fname+" "+self.lname 
    
class Products(models.Model): #('type','name','price')
    pro = [
         ('frozen food','frozen food'),
        ('fresh food','fresh food')
    ]
    type = models.CharField(max_length=50,choices=pro,verbose_name="Product Type")
    name = models.CharField(max_length=50,null=False,verbose_name="Product Name")
    price = models.DecimalField(max_digits=5,decimal_places=3)
    
    def __str__(self):
        return self.name+" "+self.type