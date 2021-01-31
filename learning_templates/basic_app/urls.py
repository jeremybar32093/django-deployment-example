from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
# NEED TO SET A GLOBAL VARIABLE NAME CALLED APP_NAME
# DJANGO WILL AUTOMATICALLY LOOK FOR THIS, SET EQUAL TO APPLICATION NAME
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'), #i.e. domain name/basic_app/relative/... will give you "relative" view
    url(r'^other/$', views.other, name='other') #i.e. domain name/basic_app/other/... will give you "other" view
]
