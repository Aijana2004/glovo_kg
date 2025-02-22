from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'courier_review', CourierReviewViewSet, basename='courier_review')
# router.register(r'courier', CourierViewSet, basename='courier')
router.register(r'store_review', StoreReviewViewSet, basename='store_review')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart_item', CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListApiView.as_view(),name=' store_list'),
    path('store/<int:pk>/', StoreDetailApiView.as_view(), name=' store_detail'),
    path('store/create/',StoreCreateApiView.as_view(),name='store_create'),
    path('store/edit/<int:pk>/',StoreUpdateDeleteApiView.as_view(),name='store_edit'),
    path('product/',ProductApiView.as_view(),name='product_list'),
    path('product/create/',ProductCreateApiView.as_view(),name='product_create'),
    path('product/edit/<int:pk>/',ProductUpdateDeleteApiView.as_view(),name='product_edit'),
    path('combo/',ProductComboApiView.as_view(),name='product_combo'),
    path('combo/create/',ProductComboCreateApiView.as_view(),name='combo_create'),
    path('combo/edit/<int:pk>/',ProductComboUpdateDeleteApiView.as_view(),name='combo_edit'),
    path('order/',OrderApiView.as_view(),name='order'),
    path('order/create/',OrderCreateApiView.as_view(),name='order_create'),
    path('order/edit/<int:pk>/',OrderEditApiView.as_view(),name='order_edit'),
    path('courier/',CourierApiView.as_view(),name='courier'),
    path('courier/create', CourierAcceptApiView.as_view(), name='courier_create'),
    path('courier/edit/<int:pk>/', CourierEditApiView.as_view(), name='courier_edit'),

]
