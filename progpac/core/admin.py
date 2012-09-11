from django.contrib import admin
from progpac.core.models import Level, Tier

admin.site.register(Tier)

class LevelAdmin(admin.ModelAdmin):
    list_filter = ('tier',)
    list_display = ('name', 'hash', 'tier')
    ordering = ('tier','name')

admin.site.register(Level, LevelAdmin)
