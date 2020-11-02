from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth.views import LoginView
from . import forms
from . import models
from . import services

#   -------------  /index  ------------- START
class Index_Page(LoginView):
    template_name = 'familytree/extends_index.html'
    extra_context = {'next': 'UserPage'}
#   -------------  /index  ------------- END

#   -------------  /index/registration ------------- START
class Registration_Page(TemplateView):
    template_name = "familytree/extends_registration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = forms.User_Registration(data = self.request.POST)
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['registration'].is_valid():
            context['registration'].save()
            return redirect('index')
        else:
            return render(request, "familytree/extends_registration.html",
                                    {'registration': context['registration']})
#   -------------  /index/registration  ------------- END

#   -------------  /index/UserPage  ------------- START
class User_Page(TemplateView):
    template_name = "familytree/extends_userpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person_create'] = forms.Person_Creation(data = self.request.POST)
        context['person_update'] = forms.Person_Update(data = self.request.POST, auto_id = False)
        context['relatives'] = models.Parents.objects.receive_person_relatives2(self.request.user.username)
        return context
    
    #Does "POST" look "clean" in terms of coding?
    #MOAR 'IF' for the IF GOD
    #Find/'write' more if-less code
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        received_button_name = request.POST['action']
        
        if received_button_name == 'LOG OUT':
            return services.log_out(request)

        if received_button_name == 'Erase account':
            return services.erase_account(request.user.username)
       
        if received_button_name == 'Add person':
            if context['person_create'].is_valid():
                context['person_create'].save(request.user.username)
                context['person_create'] = forms.Person_Creation
               
        
        if 'Update' in request.POST['action'] or 'Delete' in request.POST['action']:
            dict_key = received_button_name.lower()
            hidden_input = request.POST[dict_key].split('__')
            if context['person_update'].is_valid():
                context['person_update'].update(hidden_input)
                context['person_update'] = forms.Person_Update
            else:
                services.delete_person(hidden_input)

        return render(request, self.template_name,
                                {'person_create': context['person_create'], 'relatives':context['relatives'],
                                 'person_update': context['person_update']} )

#   -------------  /index/UserPage  ------------- END

