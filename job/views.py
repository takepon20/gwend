from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job
from django.contrib.auth.mixins import LoginRequiredMixin
# Job
# Home
class HomeJob(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'job/home_job.html'
# LIstView
class JobList(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'jobs'
    # template_name = 'job/job_list.html'
    # ログインした人の作成したJobのみ表示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = context['jobs'].filter(user=self.request.user)
        return context
# DetailView
class JobDetail(LoginRequiredMixin, DetailView):
    model = Job
    context_object_name = 'job'
# CreateView
class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['publish', 'company', 'industry', 'hp', 'title', 'country', 'city', 'occupation', 'position', 'description']
    success_url = reverse_lazy('job:list_job') #urlsのname
    # ログインした人のみ作成可能
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreate, self).form_valid(form)
# Update
class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job:list_job')
# Delete
class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job:list_job')



