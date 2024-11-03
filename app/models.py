
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinLengthValidator
# from django.db import models
# from django.conf import settings
# from django.urls import reverse
# user=settings.AUTH_USER_MODEL
STATE_CHOICE=(
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhara Pardesh','Andhara Pardesh'),
    ('Arunachal Pardesh','Arunachal Pardesh'),
    ('Asam','Asam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Punjab','Punjab'),
    ('Rajsthan','Rajsthan'),

    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal',"West Bengal"),

) 
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=50)
def __str__(self):
    return str(self.id)


CATEGORY_CHOICE=(
     ('V','Vegetable'),
     ('F','Fruits'),#Lapto
    ('TV','Top Vegetable'),
    ('BV','Bottom Vegetable'),

)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=200)
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=2)
   
    product_image=models.ImageField(upload_to='productimg')


    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
   
    quantity=models.PositiveIntegerField(default=1)    
    

    def __str__(self) :
        return str(self.id)

    # @property
    # def total_cost(self):
    #     return self.quantity*self.product.discount_price
    


STATUS_CHOICE=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    
    status=models.CharField(max_length=50,choices=STATE_CHOICE,default='Pending')

    # @property
    # def total_cost(self):
    #     return self.quantity*self.product.discount_price