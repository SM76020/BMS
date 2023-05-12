"""BMSapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from BANKapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name="HomePage"),
    path('home',views.Home),
    path('log',views.log, name="LoginPage"),
    path('Register/',views.reg, name="RegistrationPage"),
    path('dash/',views.ds,name='Dashboard'),
    path('add/',views.acc,name='Addingdata'),
    path('accdetails/',views.all_accounts,name="all accounts"),
    path('edit/<int:idp>',views.edit,name='Edit'),
    path('update/<int:idu>',views.update,name='update'),
    path('delete/<int:idd>',views.delete,name='delete'),
    path('depmoney/',views.deposit,name='Deposite'),
    path('wdmoney/',views.withdrawal,name='Withdrawl'),
    path('reports/',views.treport,name='Reports'),
    path('witdraw/',views.wit,name='wit'),
    # path('transaction-pdf',views.download_pdf,name="Download PDF"),
]
