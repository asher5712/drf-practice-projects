from rest_framework import serializers
from .models import Book, Author


class BookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)
    
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        book_mapping = {book.id: book for book in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)
            if book is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(book, data))

        # Perform deletions.
        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                book.delete()

        return ret


class BookSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(null=True)


    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'author': {
                # 'read_only': True,
            },
        }

        list_serializer_class = BookListSerializer

    


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        book_data = validated_data.pop('books')
        author = super().create(validated_data)
        
        book_data = list(map(lambda x: {'title': x['title'], 'author':author.id}, book_data))
        print(book_data)

        books = BookSerializer(data=book_data, many=True)
        books.is_valid(raise_exception=True)
        books.save()

        
        
        return author


