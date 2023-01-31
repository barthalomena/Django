from attr import field
from django import forms
from .models import Employee

class employeeform(forms.ModelForm):

    class Meta:
        model=Employee
        fields=('fullname','mobile','empcode','position')
        labels={
            'fullname':'Full Name',
            'empcode':'EMP.Code'
        }

    def __init__(self,*args,**kwargs): 
        super(employeeform,self).__init__(*args,**kwargs)  
        self.fields['position'].empty_label="select"
        self.fields['empcode'].required=False

