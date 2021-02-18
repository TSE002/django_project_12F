from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Cikkek
from .models import Kepek
from .models import Admin
from .models import Kepek_Admin

# Create your views here.
def index(request):
	# admin1 = Admin.objects.create(nev='admin',felhnev='admin',psw='admin',tel='admin',fb='admin',insta='admin')
	l = Admin.objects.get(pk=1)
	context = {'admin_list': l}
	return render(request,'index.html',context)