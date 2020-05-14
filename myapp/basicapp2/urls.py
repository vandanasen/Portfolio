#This is created
from django.conf.urls import url,include
from basicapp2 import views
app_name='basicapp2'
urlpatterns=[
            url(r'^relative/$',views.relative,name='relative'),
            url(r'^about/$',views.about,name='about'),
            url(r'^project/$',views.project,name='project'),
            url(r'^contacts/$',views.contacts,name='contacts'),
            

]