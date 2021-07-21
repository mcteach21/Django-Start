from django.contrib import admin

from .models import Post
from .models import Tag
from .models import PostTag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(PostTag)
