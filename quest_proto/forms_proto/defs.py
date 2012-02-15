# -*- coding: utf-8 -*-
default_values = {'radio': {'required': False},
                  'text': {'required': False},
                  'number': {'required': False,
                             'min_value': 0,
                             'max_value': 100}
}

definitions = [[
{
    'name': 'testi',
    'type': 'text',
    'args': {
         'max_length': 150,
    }
},
{
    'name': 'testi2',
    'type': 'radio',
    'args': {
         'choices': (('first', 'Eka'), ('second', 'Toka'))
    }
},
{
    'name': 'testi4',
    'type': 'number',
    'args':{
        'max_value': 500,
        'min_value': 5
    },
    'widget_args': {
                    'class': 'short'                    
    }
    }
],
[
{
    'name': 'testi3',
    'type': 'text',
    'args': {
             'max_length': 10,
             'required': True,
    },
    'widget_args': {
                    'class': 'short'
    }
}
],
[
{
    'name': 'testi5',
    'type': 'text',
    'args': {
             'max_length': 20
             }
},
{
    'name': 'testi6',
    'type': 'radio',
    'args': {
         'choices': (('first', 'Eka'), ('second', 'Toka'),('third', 'Kolmas'), ('fourth', 'Neljäs'))
    }
}
]
]
