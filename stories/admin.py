from django.contrib import admin

# Register your models here.
from stories.models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", 'domain', 'moderator', 'created_at', 'updated_at')
    list_filter = ("created_at", "updated_at")
    search_fields = ('title', 'moderator__username', 'moderator__first_name', 'moderator__last_name')

    fieldsets = [
        ("Story", { # title
            'fields': ('title', 'url', 'points')
        }),
        ("Moderator", {
            'classes': ('collapse',), # hide the moderator form using css
            'fields': ('moderator',)
        }),
        ("Change History", {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        })
    ]
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Story, StoryAdmin)