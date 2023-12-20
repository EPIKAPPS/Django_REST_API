from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


""" urlpatterns = [
    path('api/', views.apiOverview, name="api-overview"),
    path('api/list/', views.taskList, name="task-list"),
    path('api/detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('api/create/', views.taskCreate, name="task-create"),
    path('api/update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('api/delete/<str:pk>/', views.taskDelete, name="task-delete"),
] """