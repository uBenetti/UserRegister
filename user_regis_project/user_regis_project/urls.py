from django.urls import path
from app_user_register import views

urlpatterns = [
    # rote, main view, reference name
    # users.com
    path('',views.home,name='home'),
    # user.com/users
    path('users/', views.users, name='users_list')
]
