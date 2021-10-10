from django.urls import path
from .views import basicForm

urlpatterns = [
    path('', basicForm, name='basicForm'),

]
