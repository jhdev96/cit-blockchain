from django.urls import path
from . import views


urlpatterns = [
    path('add', views.add_record, name='add-record'),
    path('update', views.update_record, name='update-record'),
    path('delete', views.delete_record, name='delete-record')
]
