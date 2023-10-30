import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView


from users.forms import UserRegisterForm, UserProfileForm
from .models import User
from .services import send_verify_code


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verify_email', args=['code'])
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            code = secrets.token_urlsafe(nbytes=8)
            new_user.verify_code = code
            new_user.save()
            url_email = self.request.build_absolute_uri(reverse('users:verify_email', args=[code]))
            send_verify_code(new_user, url_email)
        return super().form_valid(form)


def verify(request, code):
    try:
        user = User.objects.get(verify_code=code)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))
    except User.DoesNotExist:
        return render(request, 'users/verify.html')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
