from django.urls import path
from .views import sale_list, sale_detail, sale_create, sale_update, sale_delete

app_name = "sales"

urlpatterns = [
    path('', sale_list, name='sale-list'),
    path('create/', sale_create, name='sale-create'),
    path('<int:pk>/', sale_detail, name = 'sale-detail'),
    path('<int:pk>/update/', sale_update, name = 'sale-update'),
    path('<int:pk>/delete/', sale_delete, name = 'sale-delete' )


]