from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('add-member/', views.addMember, name='addMember'),
    path('edit-member/<str:pk>', views.editMember, name='editMember'),
]