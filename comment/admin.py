from django.contrib import admin

# Register your models here.
from comment.models import Comment
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target','nickname','content','website','created_time')