from django.contrib import admin
from django.urls import path, include
from sales.views import LandingPageView, home_page 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name = 'home-page'),
    path('sales/', include('sales.urls', namespace="sales"))
]
