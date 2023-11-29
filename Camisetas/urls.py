from django.contrib import admin
from django.urls import path, include, re_path
from core.views.userView import UserListCreateView
from core.views.tipoPersonaView import TipoListCreateView
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from Camisetas.views import Inicio
from Camisetas.views import Login
from Camisetas.views import Registro


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    
    path('admin/', admin.site.urls),
    path('user/', UserListCreateView.as_view()),
    path('tipoPersona/', TipoListCreateView.as_view() ),
    path('api/category/', include ('apps.category.urls') ),
    path('inicio/', Inicio),
    path('login/', Login),
    path('registro/', Registro),
    path('api/estampado/', include ('apps.estampado.urls') ),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
