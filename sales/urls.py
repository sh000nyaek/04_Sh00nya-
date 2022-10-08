from django.urls import path
from .views import ( 
    SaleCreateView, sale_list, sale_detail, sale_create, sale_update, sale_delete, SaleListView,
    SaleDetailView, SaleUpdateView, SaleDeleteView
)
app_name = "sales"

urlpatterns = [
    path('', SaleListView.as_view(), name='sale-list'),
    path('create/', SaleCreateView.as_view(), name='sale-create'),
    path('<int:pk>/', SaleDetailView.as_view(), name = 'sale-detail'),
    path('<int:pk>/update/', SaleUpdateView.as_view(), name = 'sale-update'),
    path('<int:pk>/delete/', SaleDeleteView.as_view(), name = 'sale-delete' )


]