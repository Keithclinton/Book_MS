from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if len(value) not in [10, 13] or not value.isdigit():
            raise serializers.ValidationError()
        return value

    def validate_publication_date(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError()
        return value
