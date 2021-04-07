from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('page1/',views.page1,name="page1")
]