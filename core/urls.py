from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include(router.urls)), # e.g. /api/tasks/
path('', RedirectView.as_view(url='/api/tasks/')),
]