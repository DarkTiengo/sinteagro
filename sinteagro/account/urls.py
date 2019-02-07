from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account import views

urlpatterns = [
    path('',views.login,name="login"),
    path('cadastro',views.cadastro,name="cadastro"),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)