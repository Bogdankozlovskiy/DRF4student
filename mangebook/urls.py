from django.urls import path
from mangebook import views

urlpatterns = [
    path("list/<int:id>/", views.ListBook.as_view()),
    path("list/", views.ListBook.as_view()),
    path("create/", views.CreateBook.as_view()),
    path("delete/<str:title>/", views.DestroyBook.as_view())
]
