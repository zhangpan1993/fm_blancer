from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.view),
    url(r'^save/$',views.save),
    url(r'^status/$',views.change_status),
    url(r'^checkhttp/$',views.check_http_status),
    url(r'^delete/$',views.delete_proxy),
    url(r'^query/$',views.query_proxy),
]