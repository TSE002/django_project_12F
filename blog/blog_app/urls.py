from . import views
from django.urls import path

urlpatterns = [
	path('index',views.index,name='index'),
	path('cikkek/<int:cid>',views.cikk,name='cikk')
]
