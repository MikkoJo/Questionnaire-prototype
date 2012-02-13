# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

from defs import definitions

class QuestionnaireWizard(SessionWizardView):
    template_name= 'form_template.html'
    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
        
    def get_form_kwargs(self, step):
        return {'definition': definitions[int(step)]}
    