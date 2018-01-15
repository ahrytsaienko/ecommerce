from django.conf.urls import url

from .views import ProductListView, ProductView, ProductFeaturedView, ProductFeaturedListView, ProductSlugView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductSlugView.as_view(), name='detail'),
    url(r'f^/$', ProductFeaturedListView.as_view()),
    url(r'^(?P<pk>\d+)/$', ProductFeaturedView.as_view()),
]
