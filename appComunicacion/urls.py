from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'correo'

urlpatterns = [
    path('send/', EnviarCorreoCreateView.as_view(), ),
    path('list/', CorreoListView.as_view(), ),
    path('<pk>/update/', CorreoUpdateView.as_view(), ),
]
