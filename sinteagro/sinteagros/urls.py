"""Define os padroes de URL para sinteagros"""

from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Pagina inicial
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('ajax/get_notes/',views.get_notes,name='get_notes'),
    path('ajax/set_note/',views.set_note,name='set_note'),
    path('ajax/delete_note/',views.delete_note,name='delete_note'),
    path('ajax/get_events/',views.get_events,name='get_events'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)