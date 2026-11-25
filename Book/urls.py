from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.home, name="list"),
    path('create/', views.create, name="create"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/update/', views.update, name="update"),
]