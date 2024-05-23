from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
    path('update_user/', views.update_user, name='update_user'),
    path('performancereviewform/', views.performancereviewform, name='performancereviewform'),
    path('register', views.register_user, name='register'),
    path('employee/<str:employeeID>', views.employee, name='employee'),
    path('employees1/', views.employees1, name='employees1'),
    path('performancereviewdisplay/<int:id>', views.performancereviewdisplay, name='performancereviewdisplay'),
    path('performancereview/edit/<int:id>/', views.edit_performance_review, name='edit_performance_review'),
]



