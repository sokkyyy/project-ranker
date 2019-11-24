from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('^$',views.home, name='home'),
    re_path(r'^register/$',views.register, name='register'),
    re_path(r'^login/$',views.handle_login,name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
