"""
URL configuration for clothing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginx, name='loginx'),
    path('signup/', views.signup, name='signup'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('all_products/', views.all_products, name='all_products'),
    path('category_item/', views.category_item, name='category_item'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('cart/', views.xcart, name='cart'),
    path('handle_cart/', views.handle_cart, name='handle_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('handle_checkout/', views.handle_checkout, name='handle_checkout'),
    path('order_item/', views.order_item, name='order_item'),
    path('logout/', views.logoutx, name='logoutx'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
