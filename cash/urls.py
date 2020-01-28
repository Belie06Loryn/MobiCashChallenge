from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.page,name = 'page'),
    url(r'^add_customer/$',views.add_customer,name = 'add_customer'),
    url(r'^dele/(?P<pk>\d+)$',views.dele,name="dele"),
    url(r'^update/(?P<pk>\d+)$',views.update,name="update"),
    url(r'^view_customer/$',views.view_customer,name = 'view_customer'),
    url(r'^edit_customer/$',views.edit_customer,name = 'edit_customer'),
    url(r'^delete_customer/$',views.delete_customer,name = 'delete_customer'),
    url(r'^api/lists/$', views.AddList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)