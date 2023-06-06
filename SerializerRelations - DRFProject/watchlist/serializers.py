from rest_framework import serializers
from .models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields = '__all__'
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.StringRelatedField()
    # watchlist = serializers.PrimaryKeyRelatedField()
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        