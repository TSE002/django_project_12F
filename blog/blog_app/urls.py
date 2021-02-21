from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('',views.index,name='index'),
	path('cikkek/<int:cid>',views.cikk,name='cikk'),
	path('szerzok',views.szerzok,name='szerzok'),
	path('login',views.login,name='login'),
	path('cikk_hozzaadasa',views.check,name='check'),
	path('up_handler',views.up),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)