"""
URL configuration for society_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from societyapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('index1/',index1),
    path('index2/',index2),
    path('dashboard/',dashboard),
    path('alogin/',alogin),
    path('changepassword/',changepassword),
    
    path('aprofile/',aprofile),
    path('updateaprofile/<int:id>/',updateaprofile),
   
    path('one_committee/',one_committee),
    path('edit_one_committee/<int:id>/',edit_one_committee),

    path('one_booking/',one_booking),
    path('edit_one_booking/<int:id>/',edit_one_booking),

    path('one_function/',one_function),
    path('edit_one_function/<int:id>/',edit_one_function),

    path('one_maintenance/',one_maintenance),
    path('edit_one_maintenance/<int:id>/',edit_one_maintenance),


    path('advertisement/',advertisement),
    path('editadvertisement/<int:id>/',editadvertisement),
    path('deleteadvertisement/<int:id>/',deleteadvertisement),

    path('booking/',booking),
    path('editbooking/<int:id>/',editbooking),

    path('bookingdetail/<int:id>/',bookingdetail),
    path('editbookingdetail/<int:id>/',editbookingdetail),

    path('committee/',committee),
    path('addcommittee/',addcommittee),
    path('editcommittee/<int:id>/',editcommittee),
    path('deletecommittee/<int:id>/',deletecommittee),

    path('committeedetail/<int:id>/',committeedetail),
    path('addcommitteedetail/',addcommitteedetail),
    path('editcommitteedetail/<int:id>/',editcommitteedetail),
    path('deletecommitteedetail/<int:id>/',deletecommitteedetail),

    path('complaint/',complaint),
    path('editcomplaint/<int:id>/',editcomplaint),

    path('deposit/',deposit),
    path('adddeposit/',adddeposit),
    path('editdeposit/<int:id>/',editdeposit),
    path('deletedeposit/<int:id>/',deletedeposit),


    path('expense/',expense),
    path('addexpense/',addexpense),
    path('editexpense/<int:id>/',editexpense),
    path('deleteexpense/<int:id>/',deleteexpense),


    path('function/',function),
    path('cfunction/',cfunction),
    path('addfunction/',addfunction),
    path('editfunction/<int:id>/',editfunction),
    path('deletefunction/<int:id>/',deletefunction),


    path('item/',item),
    path('additem/',additem),
    path('edititem/<int:id>/',edititem),
    path('deleteitem/<int:id>/',deleteitem),

    path('income/',income),
    path('addincome/',addincome),
    path('editincome/<int:id>/',editincome),
    path('deleteincome/<int:id>/',deleteincome),


    path('maintenance/',maintenance),
    path('addmaintenance/',addmaintenance),
    path('editmaintenance/<int:id>/',editmaintenance),
    path('deletemaintenance/<int:id>/',deletemaintenance),

    path('member/',member),
    path('memberdetail/<int:id>/',memberdetail),
    path('addmember/',addmember),
    path('deletemember/<int:id>/',deletemember),


    path('memberfunction/<int:id>/',memberfunction),
    path('editmemberfunction/<int:id>/',editmemberfunction),

    path('membermaintenance/<int:id>/',membermaintenance),
    path('addmembermaintenance/',addmembermaintenance),
    path('editmembermaintenance/<int:id>/',editmembermaintenance),
    path('deletemembermaintenance/<int:id>/',deletemembermaintenance),


    path('notice/',notice),
    path('addnotice/',addnotice),
    path('editnotice/<int:id>/',editnotice),
    path('deletenotice/<int:id>/',deletenotice),
    
    path('occupant/',occupant),
    path('occupantdetail/<int:id>/',occupantdetail),
    path('new_main/',new_main),
    path('new_main1/',new_main1),
    path('new_main2/',new_main2),
    #member side
    path('mindex/',mindex),
    path('nindex/',nindex),
    path('madvertisement/',madvertisement),
    path('addmadvertisement/',addmadvertisement),
    path('mbooking/',mbooking),
    path('addmbooking/',addmbooking),
    path('deletembooking/<int:id>/',deletembooking),
    path('mbookingdetail/<int:id>/',mbookingdetail),
    path('addmbookingdetail/',addmbookingdetail),
    path('deletembookingdetail/<int:id>/',deletembookingdetail),
    path('mcommittee/',mcommittee),
    path('mcommitteedetail/',mcommitteedetail),
    path('mcomplaint/',mcomplaint),
    path('addmcomplaint/',addmcomplaint),
    path('mdeposit/',mdeposit),
    path('mexpense/',mexpense),
    path('mfunction/',mfunction),
    path('mincome/',mincome),
    path('mitem/',mitem),
    path('itemdetail/<int:id>/',itemdetail),
    path('mmaintenance/',mmaintenance),
    path('mmmaintenance/',mmmaintenance),
    path('mmember/',mmember),
    path('addmoccupant/',addmoccupant),
    path('editmmember/<int:id>/',editmmember),
    path('mmemberfunction/',mmemberfunction),
    path('addmmemberfunction/<int:id>/',addmmemberfunction),
    path('mmembermaintenance/',mmembermaintenance),
    path('mnotice/',mnotice),
    path('moccupant/',moccupant),
    path('editmoccupant/<int:id>/',editmoccupant),
    path('deletemoccupant/<int:id>/',deletemoccupant),
    path('editmadvertisement/<int:id>/',editmadvertisement),
    path('editmcomplaint/<int:id>/',editmcomplaint), 
    path('editmmemberfunction/<int:id>/',editmmemberfunction),
    path('editmbooking/<int:id>/',editmbooking),
    path('editmbookingdetail/<int:id>/',editmbookingdetail),
    path('mlogin/',mlogin),
    path('mloggedin/',mloggedin),
    path('mindex1/',mindex1),
    path('mindex2/',mindex2),
    path('cart/',cart),
    path('cartsave/<int:id>/',cartsave),
    path('deletecart/<int:id>/',deletecart),
    path('checkout/',checkout),
    path('binvoice/<int:id>/',invoice),
    path('home/',home),
    path('about/',about),
    path('contact/',contact),
    path('payment/',payment),
    path('search/',search),

    #visitor side
    path('vindex/',vindex),
    path('vcontact/',vcontact),
    path('vabout/',vabout),
    path('vhome/',vhome),
    path('vadvertisement/',vadvertisement),
    path('vmember/',vmember),
# Reports
    path('memberrpt/',memberrpt),
    path('occupantrpt/',occupantrpt),
    path('advertisementrpt/',advertisementrpt),
    # path('advertisementr/',advertisementr),
    path('bookingrpt/',bookingrpt),
    path('bookingdetailrpt/',bookingdetailrpt),
    path('committeerpt/',committeerpt),
    path('committeedetailrpt/',committeedetailrpt),
    path('depositrpt/',depositrpt),
    path('expenserpt/',expenserpt),
    path('functionrpt/',functionrpt),
    path('memberfunctionrpt/',memberfunctionrpt),
    path('itemrpt/',itemrpt),
    path('complaintrpt/',complaintrpt),
    path('incomerpt/',incomerpt),
    path('maintenancerpt/',maintenancerpt),
    path('membermaintenancerpt/',membermaintenancerpt),
    path('noticerpt/',noticerpt),



    

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




