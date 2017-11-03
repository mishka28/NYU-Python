from django.conf.urls import url


from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    # url(r'^link/', views.link, name='link'),
]