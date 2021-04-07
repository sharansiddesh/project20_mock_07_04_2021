from django.urls import path
from app3 import views


app_name='app3'

urlpatterns = [
    path('page3/<data>',views.page3,name="page3")
]
