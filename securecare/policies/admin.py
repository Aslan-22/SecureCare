from django.contrib import admin
from .models import Policy,Quiz

# Register your models here.
@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_at')
    search_fields = ('title', 'category')
    list_filter = ('status', 'created_at')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('policy', 'question', 'correct_option')
    list_filter = ('policy',)
    search_fields = ('question',)
