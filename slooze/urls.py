from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.home_view, name='welcome'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('products/', views.products_view, name='products'),
    path('addedit/', views.addedit_view, name='addedit'),
]