from django.urls import path
from . import views

app_name = 'pv'

urlpatterns = [
    path('', views.phrasal_verbs_view, name='phrasal_verbs'),
    path('pv/<pk>', views.phrasal_verbs_detail_view, name='phrasal_verbs_detail')
]