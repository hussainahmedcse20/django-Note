from django.shortcuts import render
from .forms import ProfileForms
from .forms import ProfileForms

def basicForm(request):
    if request.method == "POST":
        form = ProfileForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForms(request.POST)
    return render(request, 'basicForm.html',{'form':form})
