from django.urls import path
from . import views 

urlpatterns = [
    path('sign_up/',views.sign_up,name='sign_up'),
    path('',views.login_view,name='login'),
    path('login/',views.login_view,name='login'),
    path('sign_up/login/',views.login_view,name='login'),
    path('sign_up/login/index/',views.index,name='index'),
    path('login/index/',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('results/',views.extract,name='results'),
    path('index/results/',views.extract,name='results'),
     path('logout/', views.logout_view, name='logout'),
]
