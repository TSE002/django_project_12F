from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from blog_app.get_weather import getData
import pathlib
from .models import Cikkek
from .models import Kepek
from .models import Admin


def get_articles():
	a = Cikkek.objects.order_by('-datum').all()
	return a

# Create your views here.
def index(request):
	# admin1 = Admin.objects.create(nev='admin',felhnev='admin',psw='admin',tel='admin',fb='admin',insta='admin')
	#c = Cikkek.objects.create(cim='Teszt cím2',tartalom='Teszt tartalom',datum='2020-02-18',felh_id=1)
	#k = Kepek.objects.create(kep_hash='static/pictures/test.png',cikk_id=2)
	l_pic = Kepek.objects.order_by('id').all()
	a = Cikkek.objects.order_by('-datum').all()
	l = []
	for i in a:
		f = open('blog_app/static/articles/'+i.tartalom+'.txt','r',encoding='utf-8')
		dic = {'article': i, 'pic':'','content': f.read()}
		l.append(dic)
	for o in l_pic:
		for p in l:
			if p['article'].id == o.cikk_id:
				p['pic'] = o
	
	context = {'article_content':l,'weather':getData(),'all_art':get_articles()}
	return render(request,'index.html',context)

def cikk(request,cid):
	c = Cikkek.objects.get(pk=cid)
	f = open('blog_app/static/articles/'+c.tartalom+".txt","r",encoding='utf-8')
	p = Kepek.objects.get(cikk_id=c.id)
	context = {'article':c,'a_content':f.read(),'picture':p,'weather':getData(),'all_art':get_articles()}
	return render(request,'cikk.html',context)

def szerzok(request):
	users = Admin.objects.all().order_by('nev')
	context = {'u': users,'weather':getData(),'all_art':get_articles()}
	return render(request,'szerzok.html',context)
