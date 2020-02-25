from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import RegistrationForm


def RegistrationView(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST or None)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/accounts/')
    else:
        form=RegistrationForm()
    context={
    'form':form
    }
    return render(request,'accounts/registration.html',context)
