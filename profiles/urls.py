from django.urls import path
from . import views
from .views import AcademicList,AcademicDetail,AcademicCreate, AcademicUpdate, AcademicDelete, WorkList, WorkDetail, WorkCreate, WorkUpdate, WorkDelete

app_name = 'profiles'

urlpatterns = [
    # academic
    path('list-academic/', AcademicList.as_view(),name='list_academic'),
    path('detail-academic/<int:pk>', AcademicDetail.as_view(),name='detail_academic'),
    path('create-academic/', AcademicCreate.as_view(),name='create_academic'),
    path('update-academic/<int:pk>', AcademicUpdate.as_view(),name='update_academic'),
    path('delete-academic/<int:pk>', AcademicDelete.as_view(),name='delete_academic'),
    # work
    path('list-work/', WorkList.as_view(),name='list_work'),
    path('detail-work/<int:pk>', WorkDetail.as_view(),name='detail_work'),
    path('create-work/', WorkCreate.as_view(),name='create_work'),
    path('update-work/<int:pk>', WorkUpdate.as_view(),name='update_work'),
    path('delete-work/<int:pk>', WorkDelete.as_view(),name='delete_work'),
]
