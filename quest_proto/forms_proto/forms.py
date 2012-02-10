from django import forms

class questForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    #print (kwargs)
    def __init__(self, *args, **kwargs):
        print (kwargs)
        definition = kwargs.pop('definition')
        print(definition)
        super(questForm, self).__init__(*args, **kwargs)
        for dyn_field in definition:
            print(dyn_field['args'])
            self.fields[dyn_field['name']] = forms.CharField(**dyn_field['args'])
        
        
    