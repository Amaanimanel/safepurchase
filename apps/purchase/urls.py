"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.createpurchase, name='createpurchase'),
    path('current/', views.currentpurchases, name='currentpurchases'),
    path('received/', views.receivedpurchases, name='receivedpurchases'),
    path('purchase/<int:purchase_pk>', views.viewpurchase, name='viewpurchase'),
    path('purchase/<int:purchase_pk>/viewreceived', views.viewreceivedpurchase, name='viewreceivedpurchase'),
    path('purchase/<int:purchase_pk>/receive', views.receivepurchase, name='receivepurchase'),
    path('purchase/<int:purchase_pk>/delete', views.deletepurchase, name='deletepurchase'),
]
