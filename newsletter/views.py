from random import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import BlogPost
from .mixin import AddCreatorMixin, CreatorOrManagerFilterMixin, AddFromCreatorMixin, UserOwnedMixin
from .models import Client, Newsletter, Message, Log
from .forms import ClientForm, NewsletterForm, MessageForm


class HomeView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'newsletter/home.html'
    context_object_name = 'object_list'


class ClientListView(CreatorOrManagerFilterMixin, LoginRequiredMixin, ListView):
    model = Client
    template_name = 'newsletter/client_list.html'
    context_object_name = 'clients'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'newsletter/client_detail.html'
    context_object_name = 'client'


class ClientCreateView(AddCreatorMixin, LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'newsletter/client_form.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class ClientUpdateView(AddCreatorMixin, LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'newsletter/client_form.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')
    template_name = 'newsletter/client_confirm_delete.html'


class NewsletterListView(CreatorOrManagerFilterMixin, LoginRequiredMixin, ListView):
    model = Newsletter
    template_name = 'newsletter/newsletter_list.html'
    context_object_name = 'newsletters'


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    template_name = 'newsletter/newsletter_detail.html'
    context_object_name = 'newsletter'


class NewsletterCreateView(AddFromCreatorMixin, UserOwnedMixin, LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'newsletter/newsletter_form.html'
    success_url = reverse_lazy('newsletter_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs


class NewsletterUpdateView(AddFromCreatorMixin, UserOwnedMixin, LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'newsletter/newsletter_form.html'
    success_url = reverse_lazy('newsletter_list')


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter_list')
    template_name = 'newsletter/newsletter_confirm_delete.html'
    context_object_name = 'newsletter'


class MessageListView(CreatorOrManagerFilterMixin, LoginRequiredMixin, ListView):
    model = Message
    template_name = 'newsletter/message_list.html'
    context_object_name = 'messages'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'newsletter/message_detail.html'
    context_object_name = 'message'


class MessageCreateView(AddCreatorMixin, LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'newsletter/message_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('message_list')


class MessageUpdateView(AddCreatorMixin, LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'newsletter/message_update.html'


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = '/messages/'
    template_name = 'newsletter/message_confirm_delete.html'
    context_object_name = 'message'


class LogListView(LoginRequiredMixin, ListView):
    model = Log
    template_name = 'log_list.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return Log.objects.select_related('newsletter').all()


class HomeDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'newsletter/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter'] = len(Newsletter.objects.all())
        context['started_newsletter'] = Newsletter.objects.filter(is_active=True).count()
        context['client'] = len(Client.objects.all())
        context['object_list'] = random.sample(list(BlogPost.objects.all()), 3)
        return context
