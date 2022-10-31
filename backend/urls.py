from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    # User API endpoints
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),

    # User API endpoints
    path('users/', views.UserList.as_view()),

]