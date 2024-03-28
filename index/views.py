from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from job.models import Job

# Create your views here.
class Index(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'index/index.html'

class IndexDetail(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'index/index_detail.html'
