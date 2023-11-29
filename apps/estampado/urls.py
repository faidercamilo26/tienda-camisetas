from django.urls import path
from .views import EstampadoDetailView, ListEstampadoView, ListSearchView, ListRelatedView,ListBySearchView

app_name = "estampado"
urlpatterns = [
     path('estampado/<estampadoid>', EstampadoDetailView.as_view()),
    path('get-estampados', ListEstampadoView.as_view()),
    path('search', ListSearchView.as_view()),
    path('related/<estampaId>', ListRelatedView.as_view()),
    path('by/search', ListBySearchView.as_view()),
]
