from django.contrib import admin
from .models import KeywordSearch

# Register your models here.
class KeywordSearchAdmin(admin.ModelAdmin):
    readonly_fields = (
        "method",
        "created",
        "keyword",
        "language",
        "limit",
        "depth",
        "filters",
        "result",
    )
    list_display = (
        "id",
        "method",
        "created",
        "keyword",
        "language",
        "limit",
        "depth",
        "result",
    )


admin.site.register(KeywordSearch, KeywordSearchAdmin)
