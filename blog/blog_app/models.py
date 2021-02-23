from django.db import models

# Create your models here.
class Admin(models.Model):
	nev = models.CharField(max_length=255)
	felhnev = models.CharField(max_length=255)
	kep_hash = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	psw = models.CharField(max_length=255)
	tel = models.CharField(max_length=11)
	fb = models.CharField(max_length=1024)
	insta = models.CharField(max_length=1024)
	def __str__(self):
		s = str(self.id) + ' ' + self.nev + ' ' + self.felhnev + ' ' + self.tel + ' ' + self.email
		return s

class Cikkek(models.Model):
	cim = models.CharField(max_length=255)
	tartalom = models.CharField(max_length=32768)
	datum = models.DateField()
	felh = models.ForeignKey(Admin,on_delete=models.CASCADE)
	def __str__(self):
		s = str(self.id) + ' ' + self.cim + ' ' + str(self.datum) + ' '
		return s
	def get_articles(self):
		all_article = self.objects.order_by('-datum').all()
		return all_article


class Kepek(models.Model):
	kep_hash = models.CharField(max_length=255)
	cikk = models.ForeignKey(Cikkek,on_delete=models.CASCADE)
	def __str__(self):
		s = str(self.id) + ' ' + self.kep_hash + ' ' + str(self.cikk)
		return s






