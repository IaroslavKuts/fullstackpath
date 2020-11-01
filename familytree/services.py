from django.shortcuts import redirect
from django.contrib import auth
from . import forms
from . import models


def erase_account(username: str):
        models.User.objects.get(username = username).delete()
        return redirect('index')

def log_out(request):
        auth.logout(request)
        return redirect('index')

def delete_person(hidden_input: list):
    forms.kinship_dict[hidden_input[0]].filter(id = hidden_input[1]).delete()