from django.conf.urls import patterns, include, url

from forms_proto.forms import QuestForm
from forms_proto.views import QuestionnaireWizard
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quest_proto.views.home', name='home'),
    # url(r'^quest_proto/', include('quest_proto.foo.urls')),
    
    url(r'^form/$', QuestionnaireWizard.as_view([QuestForm, QuestForm]))

    #geonition urls
    #(r'^gclient/', include('geonition_client.urls')),
    #(r'^guser/', include('auth.urls')),
    #(r'^gprofile/', include('user_profile.urls')),
    #(r'^gfeature/', include('geojson_rest.urls')),
    #(r'^gemail/', include('email_rest.urls')),
    #(r'^gopen_people/', include('opensocial_people.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
