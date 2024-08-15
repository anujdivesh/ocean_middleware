"""
URL configuration for pop_middleware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from datasets.views import datasets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

admin.site.site_header = "Ocean Portal Admin"
admin.site.site_title = "Ocean Portal Middleware Portal"
admin.site.index_title = "Welcome to Ocean Portal Middleware"

urlpatterns = [
    path('middleware', datasets, name='homepage'),
    path('middleware', include('datasets.urls')),
    path('middleware', include('task_download.urls')),
    path("middleware/admin/", admin.site.urls),
    path('middleware/api/', include('datasets.urls')),
    path('middleware/api/', include('task_download.urls')),
    path('middleware/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('middleware/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('middleware', include('country.urls')),
    path('middleware/api/', include('country.urls')),
    path('middleware', include('data_type.urls')),
    path('middleware/api/', include('data_type.urls')),
    path('middleware', include('download_method.urls')),
    path('middleware/api/', include('download_method.urls')),
]
