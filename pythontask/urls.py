
from django.contrib import admin
from django.urls import path
from task import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginuser,name='loginuser'),
    path('signup/',views.signupuser,name='signupuser'),
    path('profile/',views.userprofile,name='userprofile'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('viewuser/<int:emp_pk>',views.viewuserprofile,name='viewuserprofile'),
    path('edituser/<int:emp_pk>',views.edituserprofile,name='edituserprofile'),
    path('create/',views.createprofile,name='createprofile'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)