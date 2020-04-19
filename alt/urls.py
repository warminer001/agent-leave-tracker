from django.urls import path
from alt import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('search/', views.search, name='search'),
    path('search/<int:employee_id>/', views.employee, name='employee_id'),
]