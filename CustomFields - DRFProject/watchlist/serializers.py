from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    name_length = serializers.SerializerMethodField() # Custom field for name length
    
    class Meta:
        model = Movie
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }
        
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value
        
    # Custom method for displaying the data in read only serializer method field.
    def get_name_length(self, object):
        return len(object.name)