from . import views
from django.urls import path

urlpatterns = [

path('baby',views.baby, name='baby'),
path('country',views.country, name='country'),
path('product',views.product, name='product'),




]