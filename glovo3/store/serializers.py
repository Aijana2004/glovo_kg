from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username']


class UserProfileReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name','product_photo','description','price']


class ProductCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name','product_photo','description','price']


class ProductComboSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCombo
        fields = ['combo_name','combo_photo','description','price']


class ProductComboCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCombo
        fields = ['combo_name','combo_photo','description','price']


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['contact_info']


class StoreReviewSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y ')
    user_name = UserProfileReviewSerializers()

    class Meta:
        model = StoreReview

        fields = ['user_name','rating','comment','created_date',]


class StoreListSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    count_good_grade = serializers.SerializerMethodField()


    class Meta:
        model = Store
        fields = ['id','store_name','store_image','category','avg_rating','count_people',
                  'count_good_grade']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

    def get_count_good_grade(self, obj):
        return obj.get_count_good_grade()


class StoreDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    products = ProductSerializers(many=True,read_only=True)
    combos = ProductComboSerializers(many=True,read_only=True)
    contacts = ContactInfoSerializers(many=True,read_only=True)
    reviews = StoreReviewSerializers(many= True,read_only=True)

    class Meta:
        model = Store
        fields = ['id','store_name','store_image','category','description','address','owner',
                  'products','combos','contacts','reviews']


class StoreCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name','store_image','category','description','address','owner']


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class CourierAcceptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class CourierReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourierReview
        fields = '__all__'


