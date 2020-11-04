from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from mangebook.models import Book, Comment
from mangebook.serialize import BookSerializerRead, BookSerializerWrite, CommentSerializer


class ListBook(ListAPIView):
    serializer_class = BookSerializerRead
    queryset = Book.objects


class CreateBook(CreateAPIView):
    serializer_class = BookSerializerWrite


class DestroyBook(DestroyAPIView):
    queryset = Book.objects


class UpdateBook(UpdateAPIView):
    serializer_class = BookSerializerWrite
    queryset = Book.objects


class ListComment(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects

