from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account import views

urlpatterns = [
    path('',views.login,name="login"),
    path('cadastro',views.cadastro,name="cadastro"),
    path('ajax/check_email/',views.check_email,name='check_email'),
    path('ajax/get_cidade/',views.get_cidade,name='get_cidade'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)