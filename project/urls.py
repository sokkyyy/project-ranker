from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('^$',views.home, name='home'),
    re_path(r'^register/$',views.register, name='register'),
    re_path(r'^login/$',views.handle_login,name='login'),
    path('logout/',views.handle_logout,name='logout'),
    path('profile',views.user_profile,name='profile'),
    path('profile/project/upload/',views.handle_project_upload,name='project_upload'),
    path('project/<int:project_id>/',views.project_details,name="project_details"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
