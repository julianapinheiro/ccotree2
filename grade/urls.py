# Don't forget to include in mysite/urls.py:
# url(r'', include('grade.urls'))

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.matriz, name='matriz'),
]
