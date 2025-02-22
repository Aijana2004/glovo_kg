from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'client'),
        ('courier', 'courier'),
        ('owner', 'owner'),
        ('admin', 'admin'),
    )
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Store(models.Model):
    store_name = models.CharField(max_length=25, unique=True)
    store_image = models.ImageField(upload_to= 'store_image/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    description = models.TextField()
    address = models.TextField()
    owner = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='store_owner')

    def __str__(self):
        return self.store_name

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(),1)
        return 0

    def get_count_people(self):
        total = self.reviews.all()
        if total.exists():
            if total.count() > 3:
                return '3+'
            return total.count()
        return 0

    def get_count_good_grade(self):
        total = self.reviews.all()
        if total.exists():
            num = 0
            for i in total:
                if i.rating > 3:
                    num += 1
            return f'{round((num * 100)/ total.count()) }%'

        return '0%'


class ContactInfo(models.Model):
    contact_info = PhoneNumberField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='contacts')


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='products')
    product_photo = models.ImageField(upload_to='product_photos/',null=True,blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product_name}  -  {self.store}'


class ProductCombo(models.Model):
    combo_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='combos')
    combo_photo = models.ImageField(upload_to='combo_photos/',null=True,blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.combo_name}  -  {self.store}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qyantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.qyantity


class Order(models.Model):
    STATUS_CHOICES = [
        ('	Ожидает ', 'Ожидает '),
        ('В процессе доставки', '	В процессе доставки'),
        ('•	Доставлен', '•	Доставлен'),
        ('•	Отменен ', '•	Отменен '),
    ]
    client = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='order_client')
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='Ожидает')
    delivery_address = models.CharField(max_length=70)
    courier = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='courier_name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}  - {self.status}  - {self.courier}'


class Courier(models.Model):
    STATUS_CHOICES = [
        ('доступен ', 'доступен '),
        ('занят', 'занят'),
    ]
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='courier_profile')
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='доступен')
    current_orders = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order')

    def __str__(self):
        return f'{self.user}  -  { self.status}'


class CourierReview(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField()

    def str(self):
        return f'{self.user_name}, {self.courier} - {self.rating}'


class StoreReview(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='client')
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField()

    def str(self):
        return f'{self.user_name}, {self.courier} - {self.rating}'


