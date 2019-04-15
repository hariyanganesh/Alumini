from __future__ import unicode_literals
from django.shortcuts import render, redirect   
from django.http import HttpResponse
from student.models import *
from .forms import *
from alumni.urls import *
from django.contrib.auth.decorators import login_required
from .filters import studentfilter
# Create your views here.
def display_view(request):
    if request.method == 'POST':
        print (request.POST)
        try:
            id = request.POST['records']
            print ('ID is',id)
            studinfo1.objects.filter(idnumber=int(id)).delete()
        except Exception:
            pass
                 
    x=studinfo1.objects.all()
    d={}
    d.update({'s':x})
    return render(request,'display.html',d)

def login(request):
    return render(request,'login.html',{})

def delete(request, idnumber):
    deleteobj= studinfo1.objects.filter(idnumber=idnumber).delete()
    return redirect('display')

def register_new(request):
    if request.method == "POST":
        form = StudinfoForm(request.POST)
        if form.is_valid():
            studinfo = form.save()
            studinfo.save()
            return redirect('display')
    else:
        form = StudinfoForm()
    return render(request, 'form_template.html', {'form': form})

def httpeg(request):
    x=studinfo1.objects.all()
    res="<table border=10>"
    for i in x:
        res+="<tr><td>"+i.name+"</td>"+"<td>"+i.lastname+"</td>"+"<td>"+i.idnumber+"</td>"+",<td>"+i.jobstatus+"</td>"+"<td>"+i.passout+"</td></tr>"
        res+="</table>"
    return HttpResponse(res)
    
def  get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['filter']=studentFilter(self.request.GET,queryset=self.get_queryset())
    return context
