from django.urls import path
from mangebook import views

urlpatterns = [
    path("list/<int:id>/", views.ListBook.as_view(), name="detail"),
    path("list/", views.ListBook.as_view(), name="list"),
    path("create/", views.CreateBook.as_view(), name="create"),
    path("delete/<int:pk>/", views.DestroyBook.as_view(), name="delete"),
    path("update/<int:pk>/", views.UpdateBook.as_view(), name="update"),
    path("list_comment/", views.ListComment.as_view(), name="list-comment")
]
