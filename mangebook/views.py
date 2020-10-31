from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from mangebook.models import Book
from mangebook.serialize import BookSerializer


class ListBook(ListAPIView):
    serializer_class = BookSerializer

    # queryset = Book.objects.all()
    # def get(self, request, id=None):
    #     if id is None:
    #         data = Book.objects.all()
    #         serialized_data = BookSerializer(data, many=True)
    #         return Response(serialized_data.data)
    #     data = Book.objects.get(id=id)
    #     serialized_data = BookSerializer(data)
    #     return Response(serialized_data.data)
    def get_queryset(self):
        if self.kwargs.get('id'):
            return Book.objects.filter(id=self.kwargs.get('id'))
        return Book.objects.all()


class CreateBook(CreateAPIView):
    serializer_class = BookSerializer


class DestroyBook(DestroyAPIView):
    # def get_object(self):
    #     return Book.objects.get(id=self.kwargs['id'])

    # lookup_field = 'title'
    #
    # def get_queryset(self):
    #     return Book.objects.all()

    def delete(self, request, title):
        Book.objects.filter(title=title).delete()
        return Response({"ok": True})


class UpdateBook(UpdateAPIView):
    def get_object(self):
        pass
# Create your views here.
