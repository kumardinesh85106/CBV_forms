from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/Home.html'

class CollegeList(ListView):
    model=College
    context_object_name='colleges'


class CollegeDetail(DetailView):
    model=College
    context_object_name ='collegeobj'



class CollegeCreate(CreateView):
    model=College
    fields='__all__'

class CollegeUpdate(UpdateView):
    model=College
    fields='__all__'

class CollegeDelete(DeleteView):
    model=College
    context_object_name='collegeobject'
    success_url= reverse_lazy('CollegeList')
