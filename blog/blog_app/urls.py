from . import views
from django.urls import path

urlpatterns = [
	path('',views.index,name='index'),
	path('cikkek/<int:cid>',views.cikk,name='cikk'),
	path('szerzok',views.szerzok,name='szerzok'),
	path('login',views.login,name='login'),
	path('cikk_hozzaadasa',views.check,name='check'),
]
