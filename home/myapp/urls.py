from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('about/', views.about, name='about'),
                  path('all_order_client/<int:client_id>/', views.all_orders_by_client, name='all_orders_by_client'),
                  path('all_orders_client_sort/<int:client_id>/', views.all_orders_client_sort,
                       name='all_orders_client_sort'),
                  path('product_add/', views.product_add, name='product_add'),
                  path('product/<int:product_id>/', views.product_view, name='product_view'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

