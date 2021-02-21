from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import loader
from django.http import HttpResponse
from django import forms
from blog_app.get_weather import getData
from .models import Cikkek
from .models import Kepek
from .models import Admin
import datetime


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
		f = open(i.tartalom,'r',encoding='utf-8')
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
	f = open(c.tartalom,"r",encoding='utf-8')
	p = Kepek.objects.get(cikk_id=c.id)
	u = Admin.objects.get(pk=c.felh_id)
	context = {'article':c,'a_content':f.read(),'picture':p,'weather':getData(),'all_art':get_articles(),'writer':u}
	return render(request,'cikk.html',context)

def szerzok(request):
	users = Admin.objects.all().order_by('nev')
	context = {'u': users,'weather':getData(),'all_art':get_articles()}
	return render(request,'szerzok.html',context)

def login(request):
	return render(request,'login.html')

def check(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		f = Admin.objects.filter(felhnev=username).filter(psw=password)
		if f:
			context = {'user_id':f}
			return render(request,'cikk_hozzaadasa.html',context)
		else:
			return redirect('/login',permanent=True)
	else:
		return redirect('/login',permanent=True)


def up(request):
	if request.method == 'POST' and request.FILES['kep']:
		f = request.FILES['kep']
		fs = FileSystemStorage()
		fs.save('pictures/'+f.name,f)
		title = request.POST['cim']
		content = request.POST['tartalom']
		text = open('media/articles/'+title+'.txt','w',encoding='utf-8')
		text.write(content)
		d = datetime.datetime.now().strftime('%Y-%m-%d')
		article = Cikkek.objects.create(cim=title,tartalom='media/articles/'+title+'.txt',datum=d,felh_id=request.POST['user_id'])
		a = Cikkek.objects.filter(cim=title).filter(tartalom='media/articles/'+title+'.txt').filter(datum=d)
		picture = Kepek.objects.create(kep_hash=f.name,cikk_id=a[0].id)
		return render(request,'cikk_hozzaadasa.html')
	else:
		return HttpResponse('Err')