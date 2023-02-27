from django.forms import ModelForm
from .models import Account
from django import forms




class Registrationform(ModelForm):
    password= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))

    password2= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    
    class Meta:
        model=Account
        widgets = {
            'first_name' : forms.TextInput(attrs = {'placeholder': 'first-name'}),
            'last_name'    : forms.TextInput(attrs = {'placeholder': 'last-name'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
        }
        fields=['first_name','last_name','email','phone_number','password','password2']


    # to override the class property
    def __init__(self, *args,**kwargs):
        super(Registrationform, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        data = super(Registrationform,self).clean()
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("password does't match! ")
        return data