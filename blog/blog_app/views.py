from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from blog_app.get_weather import getData
from .models import Cikkek
from .models import Kepek
from .models import Admin
from .models import Kepek_Admin

# Create your views here.
def index(request):
	# admin1 = Admin.objects.create(nev='admin',felhnev='admin',psw='admin',tel='admin',fb='admin',insta='admin')
	#c = Cikkek.objects.create(cim='Teszt cím2',tartalom='Teszt tartalom',datum='2020-02-18',felh_id=1)
	#k = Kepek.objects.create(kep_hash='static/pictures/test.png',cikk_id=2)
	l_pic = Kepek.objects.order_by('id').all()
	a = Cikkek.objects.order_by('id').all()
	l = []
	for i in a:
		dic = {'article': i, 'pic':''}
		l.append(dic)
	for o in l_pic:
		for p in l:
			if p['article'].id == o.cikk_id:
				p['pic'] = o
	context = {'article_content':l,'weather':getData()}
	return render(request,'index.html',context)