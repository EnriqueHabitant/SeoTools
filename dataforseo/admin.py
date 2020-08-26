from django.contrib import admin
from .models import KeywordSearch, KeywordList

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

class KeywordListAdmin(admin.ModelAdmin):
    readonly_fields = (
        "method",
        "created",
        "keywords",
        "language",
        "result",
        "user",
    )
    list_display = (
        "id",
        "method",
        "created",
        "keywords",
        "language",
        "result",
        "user",
    )


admin.site.register(KeywordSearch, KeywordSearchAdmin)
admin.site.register(KeywordList, KeywordListAdmin)