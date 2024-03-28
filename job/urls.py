from django.urls import path
from . import views
from .views import JobList,JobDetail,JobCreate, JobUpdate, JobDelete, HomeJob

app_name = 'job'

urlpatterns = [
    path('home_job', HomeJob.as_view(), name='home_job'),
    path('list-job', JobList.as_view(),name='list_job'),
    path('detail-job/<int:pk>', JobDetail.as_view(),name='detail_job'),
    path('create-job/', JobCreate.as_view(),name='create_job'),
    path('update-job/<int:pk>', JobUpdate.as_view(),name='update_job'),
    path('delete-job/<int:pk>', JobDelete.as_view(),name='delete_job'),
]