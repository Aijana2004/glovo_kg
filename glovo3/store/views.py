from rest_framework import viewsets,generics,permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import CategoryFilter
from .permissions import (CheckCreateStore,CheckOwnerStore,CheckCreateAllProduct,CheckOwnerAllProduct,CheckCreateOrder,
                          CheckOwnerOrder,CheckCreateCourier,CheckOwnerCourier,CheckReviewCourier)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filterset_class = CategoryFilter


class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializers
    search_fields =['store_name']


class StoreDetailApiView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializers


class StoreCreateApiView(generics.CreateAPIView):
    serializer_class = StoreCreateSerializers
    permission_classes = [CheckCreateStore]


class StoreUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreCreateSerializers
    permission_classes = [CheckCreateStore,CheckOwnerStore]


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]


class ProductCreateApiView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializers
    permission_classes = [CheckCreateAllProduct]


class ProductUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers
    permission_classes = [CheckCreateAllProduct,CheckOwnerAllProduct]


class ProductComboApiView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializers


class ProductComboCreateApiView(generics.CreateAPIView):
    serializer_class = ProductComboCreateSerializers
    permission_classes = [CheckCreateAllProduct]


class ProductComboUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboCreateSerializers
    permission_classes = [CheckCreateAllProduct,CheckOwnerAllProduct]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers


class OrderApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderCreateApiView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializers
    permission_classes = [CheckCreateOrder]


class OrderEditApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializers
    permission_classes = [CheckCreateOrder,CheckOwnerOrder]


class CourierApiView(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializers


class CourierAcceptApiView(generics.CreateAPIView):
    serializer_class = CourierAcceptSerializers
    permission_classes = [CheckCreateCourier]


class CourierEditApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierAcceptSerializers
    permission_classes = [CheckCreateCourier,CheckOwnerCourier]


class CourierReviewViewSet(viewsets.ModelViewSet):
    queryset = CourierReview.objects.all()
    serializer_class = CourierReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,CheckReviewCourier]


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializers




