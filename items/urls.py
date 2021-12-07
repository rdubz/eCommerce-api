from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('', views.get_items, name='get_items'),
    path('<int:item_id>/', views.get_item, name='get_item'),
    path('add/', views.add_item, name='add_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
]
