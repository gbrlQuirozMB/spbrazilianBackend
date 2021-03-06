from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'empleo'

urlpatterns = [
    path('solicitud/create/', SolicitudCreateView.as_view(), ),
    path('solicitud/<pk>/detail/', SolicitudDetailView.as_view(), ),
    path('solicitud-admin/<pk>/update/', SolicitudAdminUpdateView.as_view(), ),
    path('solicitud/list/', SolicitudListView.as_view(), ),
]
