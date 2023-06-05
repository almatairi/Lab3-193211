from django.urls import path

from . import views

urlpatterns = [
    path('register/',views.register ,name='register'),
    path('login/',views.logInUser ,name='login'),
    path('logout/',views.UserLogOut ,name='logout'),

    path('profile/<str:pk>/',views.viewProfile ,name='profile'),
    path('edit-profile/', views.editProfile , name='edit-profile'),
]