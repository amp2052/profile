from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'ip_address',
        'path',
        'visit_count',
        'first_visit',
        'last_visit',
        'short_user_agent'
    )
    list_filter = ('path', 'ip_address', 'first_visit')
    search_fields = ('ip_address', 'path', 'user_agent')

    def short_user_agent(self, obj):
        return obj.user_agent[:50] + "..."
    short_user_agent.short_description = "User Agent"
