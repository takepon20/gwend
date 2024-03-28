
from django.contrib import admin
from django.urls import path, include
# sqライトに修正した
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('accounts/', include('account.urls')),
    path('job/', include('job.urls')),
    path('profiles/', include('profiles.urls')),
]
