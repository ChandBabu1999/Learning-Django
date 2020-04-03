from django.urls import path

from . import views

app_name = 'app'

# urlpatterns = [
#     # ex: /app/
#     path('', views.index, name='index'),
#     # ex: /app/5/
#     path('<int:pk>/', views.detail, name='detail'),
#     # ex: /app/5/results/
#     path('<int:pk>/results/', views.results, name='results'),
#     # ex: /app/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]