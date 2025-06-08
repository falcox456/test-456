from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.not_port, name='index'),
    path('register/',views.register, name='index'),
    path('login/', views.log_in, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.register, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)