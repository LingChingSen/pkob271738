from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('ic_no','name','phone','address1','address2','city','mukim','parlimen','state','poskod','income')
        labels={
            'ic_no': '',
            'name': '',
            'phone': '',
            'address1': '',
            'address2': '',
            'city': '',
            'mukim': '',
            'parlimen': '',
            'state': '',
            'poskod': '',
            'income': '',
        }
        widgets ={
            'ic_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ic number'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone'}),
            'address1':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address 1'}),
            'address2':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address 2'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter city'}),
            'mukim':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter mukim'}),
            'parlimen':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter parlimen'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter state'}),
            'poskod':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter poskod'}),
            'income':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter income'}),
        }

class UpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ('ic_no', 'name', 'phone', 'address1', 'address2', 'city', 'mukim', 'parlimen', 'state', 'poskod', 'income')

    def __init__(self, *args, **kwargs):
     super(UpdateForm, self).__init__(*args, **kwargs)
     self.fields['ic_no'].widget.attrs['readonly'] = True
     self.fields['name'].widget.attrs['readonly'] = True
     self.fields['address1'].widget.attrs['readonly'] = True
     self.fields['address2'].widget.attrs['readonly'] = True
     self.fields['city'].widget.attrs['readonly'] = True
     self.fields['mukim'].widget.attrs['readonly'] = True
     self.fields['parlimen'].widget.attrs['readonly'] = True
     self.fields['state'].widget.attrs['readonly'] = True
     self.fields['poskod'].widget.attrs['readonly'] = True
     self.fields['income'].widget.attrs['readonly'] = True
