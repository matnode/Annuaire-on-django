# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from User.models import User, Lieu


def index(request):
	My_contact_list= User.objects.all()
	t = loader.get_template('userhtml/index.html')
	c = Context({
		'My_contact_list': My_contact_list,
	})
	return HttpResponse(t.render(c))


def regisuser(request):	
	#maintenant on ne prefixe plus le lieu l'utilisateur le fait lui-meme
	leslieux= Lieu.objects.all()
	
	#on se rassure que la requete qui arrive est de type post
	if request.method == 'POST':	
		u = User(
			lieu = Lieu.objects.get(pk=request.POST['lieu']),
			Nom = request.POST['Nom'],
			Prenom = request.POST['Prenom'],
			Age = request.POST['Age'],
			date_creation = timezone.now(),
			)
		u.save()
		return HttpResponseRedirect(reverse('User.views.index'))

	return render_to_response('userhtml/regisuser.html', {'leslieux':leslieux}, context_instance=RequestContext(request))


def detail(request, user_id):
	contact = User.objects.get(pk=user_id)
	t = loader.get_template('userhtml/detail.html')
	c = Context({
		'contact': contact,
	})
	return HttpResponse(t.render(c))


def regislieu(request):	
	
	leslieux= Lieu.objects.all()		
	#on se rassure que la requete qui arrive est de type post
	if request.method == 'POST':	
		l = Lieu(
			
			Pays = request.POST['Pays'],
			Region = request.POST['Region'],
			Ville = request.POST['Ville'],
			
			)
		l.save()
		return HttpResponseRedirect(reverse('User.views.regislieu'))

	return render_to_response('userhtml/regislieu.html', {'leslieux':leslieux}, context_instance=RequestContext(request))




