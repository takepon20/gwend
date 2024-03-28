from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Academic, Work
from django.contrib.auth.mixins import LoginRequiredMixin

# Academic
# LIstView
class AcademicList(LoginRequiredMixin, ListView):
    model = Academic
    context_object_name = 'Academics'
    # ログインした人の作成したJobのみ表示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Academics'] = context['Academics'].filter(user=self.request.user)
        return context
# DetailView
class AcademicDetail(LoginRequiredMixin, DetailView):
    model = Academic
    context_object_name = 'academic'
# CreateView
class AcademicCreate(LoginRequiredMixin, CreateView):
    model = Academic
    fields = ['publish', 'school', 'type', 'hp', 'country', 'city', 'status', 'admission_date', 'graduation_date', 'description']
    success_url = reverse_lazy('profiles:list_academic') #urlsのname
    # ログインした人のみ作成可能
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AcademicCreate, self).form_valid(form)
# Update
class AcademicUpdate(LoginRequiredMixin, UpdateView):
    model = Academic
    fields = '__all__'
    success_url = reverse_lazy('profiles:list_academic')
# Delete
class AcademicDelete(LoginRequiredMixin, DeleteView):
    model = Academic
    fields = '__all__'
    success_url = reverse_lazy('profiles:list_academic')



# Work
# LIstView
class WorkList(LoginRequiredMixin, ListView):
    model = Work
    context_object_name = 'Works'
    # ログインした人の作成したJobのみ表示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Works'] = context['Works'].filter(user=self.request.user)
        return context
# DetailView
class WorkDetail(LoginRequiredMixin, DetailView):
    model = Work
    context_object_name = 'work'
# CreateView
class WorkCreate(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['publish', 'company', 'industry', 'hp', 'title', 'country', 'city', 'occupation', 'position', 'description', 'joining_date', 'leaving_date']
    success_url = reverse_lazy('profiles:list_work') #urlsのname
    # ログインした人のみ作成可能
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkCreate, self).form_valid(form)
# Update
class WorkUpdate(LoginRequiredMixin, UpdateView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('profiles:list_work')
# Delete
class WorkDelete(LoginRequiredMixin, DeleteView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('profiles:list_work')
