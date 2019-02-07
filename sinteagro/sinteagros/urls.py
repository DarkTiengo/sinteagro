"""Define os padroes de URL para sinteagros"""

from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Pagina inicial
    path('',views.index,name='index'),
    path('index/<alert>/',views.index,name='index'),
    path('cadastrar_fazenda',views.cadastrar_fazenda,name='cadastrar_fazenda'),
    path('fazenda/<fazenda_id>/',views.fazenda,name='fazenda'),
    path('fazenda/<fazenda_id>/<alert>/',views.fazenda,name='fazenda'),
    path('edit_fazenda/<fazenda_id>/',views.edit_fazenda,name='edit_fazenda'),
    path('talhao/<fazenda_id>/<talhao_id>/',views.talhao,name='talhao'),
    path('cadastrar_talhao/<fazenda_id>/',views.cadastrar_talhao,name='cadastrar_talhao'),
    path('safra/',views.safra,name='safra'),
    path('cadastrar_safra/',views.cadastrar_safra,name='cadastrar_safra'),
    path('logout/',views.logout,name='logout'),
    path('exclui_fazenda/<fazenda_id>/',views.exclui_fazenda,name='exclui_fazenda'),
    path('configuracoes/',views.configuracoes,name='configuracoes'),
    path('altera_senha/',views.altera_senha,name='altera_senha'),
    path('edit_talhoes/<fazenda_id>/',views.edit_talhoes,name='edit_talhoes'),
    path('edit_talhao/<fazenda_id>/<talhao_id>/',views.edit_talhao,name='edit_talhao'),
    path('apaga_talhao/<fazenda_id>/<talhao_id>/',views.apaga_talhao,name='apaga_talhao'),
    path('edit_produtividades/<fazenda_id>/<talhao_id>/',views.edit_produtividades,name='edit_produtividades'),
    path('edit_producao/<fazenda_id>/<talhao_id>/',views.edit_producao,name='edit_producao'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)