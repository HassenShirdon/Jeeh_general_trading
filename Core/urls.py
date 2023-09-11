from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('products', views.product, name='product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/edit/<int:id>/', views.edit_product, name='product-edit'),
    path('product/delete/<int:id>/', views.delete_product, name='product-delete'),
    path('product/create', views.create_product, name='product-create'),
    path('team/create', views.create_team, name='team-create'),
    path('testimonial/create', views.create_testimonials,
         name='testimonial-create'),

]
