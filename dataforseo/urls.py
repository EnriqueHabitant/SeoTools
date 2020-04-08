from django.urls import path
from .views import KeywordFinderCreateView, related_keywords, KeywordFinderDetailView

dataforseo_patterns = (
    [
        path("", KeywordFinderCreateView.as_view(), name="keywordsearch"),
        path("<int:pk>/", KeywordFinderDetailView.as_view(), name="keywordsearch_detail"),
        # path('related_keywords/', KeywordFinderCreateView.as_view()),
        path('related_keywords/<keyword>/<country_code>/<language_code>/<int:depth>/<int:limit>/', related_keywords),
    ],
    "dataforseo",
)
