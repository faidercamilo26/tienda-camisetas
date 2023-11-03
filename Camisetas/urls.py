from django.contrib import admin
from django.urls import path, include, re_path
from core.views.userView import UserListCreateView
from core.views.tipoPersonaView import TipoListCreateView
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    
    path('admin/', admin.site.urls),
    path('user/', UserListCreateView.as_view()),
    path('tipoPersona/', TipoListCreateView.as_view() ),
]
