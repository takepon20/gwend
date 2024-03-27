from django.urls import path
from .views import Index, IndexDetail

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail-index/<int:pk>/', IndexDetail.as_view(), name='detail_index'),
]