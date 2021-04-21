from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import StudentRegister
from .models import User

# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(username=nm, email=em, password=pas)
            reg.save() 
            fm = StudentRegister() 
    else:
        fm = StudentRegister()
    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stud':stu})

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegister(instance=pi)

    return render(request, 'enroll/update.html', {'form':fm, 'id':id})


