from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role')
    list_editable = ('role',)
    list_filter = ('role',)
    ordering = ('id',)


class CategoryGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_editable = ('name', 'slug')
    ordering = ('id',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'category')
    list_editable = ('year', 'category')
    list_filter = ('category', 'year')
    ordering = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'title', 'author', 'score')
    list_filter = ('author',)
    ordering = ('id',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'review', 'author',)
    list_filter = ('author',)
    ordering = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryGenreAdmin)
admin.site.register(Genre, CategoryGenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
