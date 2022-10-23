from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view, name='Index'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('menu/', views.menu, name='menu'),
    path('reservation/',views.reservation, name='reservation'),
    path('about_us/',views.about_us, name='about_us')
]