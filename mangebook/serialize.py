from rest_framework.serializers import ModelSerializer
from mangebook.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'text', 'date')
