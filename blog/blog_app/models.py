from django.db import models

# Create your models here.
class Admin(models.Model):
	nev = models.CharField(max_length=255)
	felhnev = models.CharField(max_length=255)
	psw = models.CharField(max_length=255)
	tel = models.CharField(max_length=11)
	fb = models.CharField(max_length=1024)
	insta = models.CharField(max_length=1024)
	pic_id = models.ForeignKey('Kepek',on_delete=models.CASCADE)

class Cikkek(models.Model):
	cim = models.CharField(max_length=255)
	tartalom = models.CharField(max_length=32768)
	datum = models.DateField()
	felh_id = models.ForeignKey(Admin,on_delete=models.CASCADE)


class Kepek(models.Model):
	kep_hash = models.CharField(max_length=255)
	cikk_id = models.ForeignKey(Cikkek,on_delete=models.CASCADE)






