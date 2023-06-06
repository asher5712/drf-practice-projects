from django.contrib import admin
from .models import WatchList, StreamPlatform

# Register your models here.

# Registering WatchList model in admin site
admin.site.register(WatchList)
# Registering StreamPlatform model in admin site
admin.site.register(StreamPlatform)
