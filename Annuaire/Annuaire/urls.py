from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Annuaire.views.home', name='home'),
    # url(r'^Annuaire/', include('Annuaire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^user/$', 'User.views.index'),
    url(r'^user/newuser/$', 'User.views.regisuser'),
    url(r'^user/(?P<user_id>\d+)/detail/$', 'User.views.detail'),
    url(r'^lieu/newlieu/$', 'User.views.regislieu')
)
