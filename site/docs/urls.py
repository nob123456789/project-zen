from django.urls import path
from . import views

app_name = 'docs'

urlpatterns = [
    path('<slug:name>/', views.locator, name="locator"),
]