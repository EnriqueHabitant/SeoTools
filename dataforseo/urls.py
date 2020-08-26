from django.urls import path
from .views import *

#
PATH_KEYWORD = 'keyword-research/'

PATH_FINDER = "keyword-finder/"
PATH_BULK = "keyword-list/"
PATH_SERP = "serp-compare/"

dataforseo_patterns = (
    [
        # URLs de keyword-finder
        path(PATH_KEYWORD+PATH_FINDER, KeywordFinderCreateView.as_view(), name="keywordfinder"),
        path(PATH_KEYWORD+PATH_FINDER+'<int:pk>/', KeywordFinderDetailView.as_view(), name="keywordfinder_detail"),
        path(PATH_KEYWORD+PATH_FINDER+'<keyword>/<country_code>/<language_code>/<int:depth>/<int:limit>/<filters>', keyword_research),

        # URLs de keyword-bulk
        path(PATH_KEYWORD+PATH_BULK, KeywordBulkCreateView.as_view(), name="keywordbulk"),
        path(PATH_KEYWORD+PATH_BULK+'<int:pk>/', KeywordBulkDetailView.as_view(), name="keywordbulk_detail"),
        path(PATH_KEYWORD+PATH_BULK+'<keywords>/<country_code>/<language_code>', keyword_list),

        # URLs de SERP
        path(PATH_SERP, KeywordBulkCreateView.as_view(), name="serp_compare"),

        # URLs includes
        path(PATH_KEYWORD+'includes/filter/', Filter.as_view()),
        path(PATH_KEYWORD+'includes/loading/', Loading.as_view()),
    ],
    "dataforseo",
)
