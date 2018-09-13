from django.conf.urls import url
from django.contrib import admin
from books.views import PublisherList
from books.views import PublisherBookList


from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$',views.index,name='index'),
    url(r'^search/$', views.search),
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^books/([\w-]+)/$', PublisherBookList.as_view()),
    url( r'^editdetails/(\d+)/$',views.editdetails, name="editdetails"),
    url( r'^deletedetails/(\d+)/$',views.deletedetails, name="deletedetails"),
    url( r'^update/$',views.update, name="update")
]
