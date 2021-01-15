from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tableau', views.tableau, name='tableau'),
    path('statistics', views.statistics, name='statistics'),
] 
