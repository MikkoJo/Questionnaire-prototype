from django import forms
from widgets import NumberInput

from defs import default_values
#from defs import definitions

class QuestForm(forms.Form):
    #name = forms.CharField(required=False, max_length=100)
    #print (kwargs)
    def __init__(self, *args, **kwargs):
#        print (kwargs)
        definition = kwargs.pop('definition')
#        print(definition)
        super(QuestForm, self).__init__(*args, **kwargs)
        for dyn_field in definition:
#            print(dyn_field['args'])
            # Check the type and choose field and widget
            field_type = dyn_field['type']
            field_args = dict(default_values[field_type])
            if('args' in dyn_field):
                field_args.update(dyn_field['args'])
            #print (field_args)
            #widget_args = dict(default_values[field_type])
            widget_args = dict()
            if('widget_args' in dyn_field):
                widget_args.update(dyn_field['widget_args'])
            #print (widget_args)
            if(field_type == 'radio'):
                self.fields[dyn_field['name']] = forms.ChoiceField(widget=forms.RadioSelect(attrs=widget_args), **field_args)
            elif(field_type == 'text'):
                self.fields[dyn_field['name']] = forms.CharField(widget=forms.TextInput(attrs=widget_args), **field_args)
            elif(field_type == 'number'):
                self.fields[dyn_field['name']] = forms.IntegerField(widget=NumberInput(attrs=widget_args), **field_args)
            
            #self.fields[dyn_field['name']] = forms.CharField(**dyn_field['args'])
        
        
    