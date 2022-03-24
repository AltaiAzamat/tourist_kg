from django.urls import path
from account.views import register, sign_in, logout_user


urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', register, name = 'register')
]


