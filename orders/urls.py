from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create-promo-code/', views.create_promo_code, name='create_promo_code'),
    path('update-promo-code/<int:promo_code_id>/', views.update_promo_code, name='update_promo_code'),
    path('delete-promo-code/<int:promo_code_id>/', views.delete_promo_code, name='delete_promo_code'),
]
