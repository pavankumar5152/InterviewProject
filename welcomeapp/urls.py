from django.conf.urls import url
from . import views
urlpatterns=[

    url(r'^home',views.home),
    url(r'^company/',views.company),
    url(r'^programs/',views.programs),

]