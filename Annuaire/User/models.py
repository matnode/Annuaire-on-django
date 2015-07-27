from django.db import models
import datetime
# Create your models here.
class Lieu(models.Model):
	Pays = models.CharField(max_length=200)
	Region = models.CharField(max_length=200)
	Ville = models.CharField(max_length=200)
	def __unicode__(self):
	 	return self.Pays
	def __unicode__(self):
		return self.Region
	def __unicode__(self):
		return self.Ville

class User(models.Model):
	lieu = models.ForeignKey(Lieu)
	Nom = models.CharField(max_length=200)
	Prenom = models.CharField(max_length=200)
	Age = models.IntegerField(max_length=11)
	date_creation = models.DateTimeField('date published')
	def __unicode__(self):
		return self.Nom
	def __unicode__(self):
		return self.Prenom
	def was_published_today(self):
		return self.date_creation.date() == datetime.date.today()
