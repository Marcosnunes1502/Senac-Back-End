from django.urls import path
from primeiro_app import views

urlpatterns = [
    path("", views.home),
    path("listagem/", views.listagem, name="url_listagem"),
    path("form/", views.criar),
    path("novo/", views.criar, name="url_novo"),
    path("update/<int:pk>", views.update, name="url_update"),
    path("delete/<int:pk>", views.delete, name="ulr_delete")

]