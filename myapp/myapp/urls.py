from django.contrib import admin
from django.urls import path
from basicapp2 import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^basicapp2/', include('basicapp2.urls')),
    url(r'^$',views.project,name='project'),
    url(r'^$',views.contacts,name='contacts')
]