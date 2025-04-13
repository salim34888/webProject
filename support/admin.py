from django.contrib import admin
from .models import FAQCategory, FAQ, SupportTicket

class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [FAQInline]

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    list_editable = ('order',)

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('subject', 'message', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'subject', 'message', 'status')
        }),
        ('Ответ поддержки', {
            'fields': ('admin_response',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        })
    )