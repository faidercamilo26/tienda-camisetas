from django.contrib import admin
from django.urls import path
from core.views.userView import UserListCreateView
from core.views.tipoPersonaView import TipoListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserListCreateView.as_view()),
    path('tipoPersona/', TipoListCreateView.as_view() ),
    
]
