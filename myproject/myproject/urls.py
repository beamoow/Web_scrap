"""myproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from myapp import views

from django.conf import settings
from django.conf.urls.static import static

from myapp.views import ItemListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ItemListView.as_view(), name='home'),
    # path('',views.all_products, name='all_products'),
    # path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    # path('item/<slug:slug>/', views.product_detail , name='product_detail'),
    path('profile/',views.profile, name='profile'),
    path("accounts/signup/", views.register_request, name="register"),
    path("accounts/login/", views.login_request, name="login"),
    path("accounts/logout/", views.logout_request, name= "logout"),
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

