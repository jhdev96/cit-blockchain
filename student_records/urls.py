from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_record, name='add-recod'),
    path('update', views.update_record, name='update-record'),
    path('delete', views.delete_record, name='delete-record')
]
