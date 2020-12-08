from django.forms import ModelForm, Form
from django import forms
from django.conf import settings
from .models import Person, Parents, Siblings, Grand_Parents, Spouse
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError


kinship_dict = {'Parents': Parents,
                'Grand_parents': Grand_Parents,
                'Siblings': Siblings,
                'Spouse': Spouse}

    
class User_Registration(Form):
    #form internet
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  forms.ValidationError("Username already exists")
        return username


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  forms.ValidationError("Email already exists")
        return email


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2


    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
 

class Person_Creation(ModelForm):
    kinship = forms.ChoiceField(choices = settings.KINSHIP_CHOICES, widget = forms.RadioSelect)
    class Meta:
        model = Person
        exclude = ['belongs_to_user']
        widgets = {
            'person_birthdate': forms.DateInput(attrs={'type': 'date'})
        }

    
    def clean_kinship(self):
        POSTed = self.cleaned_data['kinship']
        return kinship_dict[POSTed].create

    def save(self, username):
        save_person = self.cleaned_data['kinship']
        obtained_person_fields = {}
        for index in range(len(settings.PERSON_FIELDS)-1):
            obtained_person_fields[settings.PERSON_FIELDS[index]] = self.cleaned_data[settings.PERSON_FIELDS[index]]
        obtained_person_fields['belongs_to_user'] = User.objects.get(username = username)   
        save_person(**obtained_person_fields)


class Person_Update(Form):
    radio_dots = forms.ChoiceField(choices = settings.DOT_CHOICES, widget = forms.RadioSelect)
    user_input = forms.CharField(max_length=150)


    def clean_radio_dots(self):
        chosen_field = settings.PERSON_FIELDS[int(self.cleaned_data['radio_dots'])]
        return chosen_field

    def clean_user_input(self):
        user_input = self.cleaned_data['user_input']
        return user_input

    def update(self, secondary_data: list):
        chosen_field = self.cleaned_data['radio_dots']
        person_id = secondary_data[1]
        user_input = self.cleaned_data['user_input']
        chosen_kinship = secondary_data[0]
        field_input = {chosen_field : user_input}
        kinship_dict[chosen_kinship].objects.filter(id = person_id).update(**field_input)
        