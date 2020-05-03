from django.urls import path
from .views import *

PATH_FINDER = "keyword-finder/"
PATH_BULK = "keyword-list/"

dataforseo_patterns = (
    [
        # URLs de keyword-finder
        path(PATH_FINDER, KeywordFinderCreateView.as_view(), name="keywordfinder"),
        path(PATH_FINDER+'<int:pk>/', KeywordFinderDetailView.as_view(), name="keywordfinder_detail"),
        path(PATH_FINDER+'<keyword>/<country_code>/<language_code>/<int:depth>/<int:limit>/<filters>', keyword_research),

        # URLs de keyword-bulk
        path(PATH_BULK, KeywordBulkCreateView.as_view(), name="keywordbulk"),

        # URLs includes
        path('includes/filter/', Filter.as_view()),
        path('includes/loading/', Loading.as_view()),
    ],
    "dataforseo",
)
