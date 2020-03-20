from django.urls import path
from .import views

from Probad.views import data, district, chondokotha, lazy_eagar, place

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('data/', data),
    path ('district/', district),
    path ('chondokotha/', chondokotha),
    path ('lazy/', lazy_eagar),
    path ('resturant/', place)


]
# urlpatterns = []
