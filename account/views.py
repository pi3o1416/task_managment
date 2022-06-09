
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from .forms import UserForm, UserCreateForm
from .models import User


class CreateUser(View):
    form_class = UserCreateForm
    template_name = 'account/create_account.html'

    def get(self, request, format=None):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, format=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect(reverse('account:login'))
        return render(request, self.template_name, {'form': form})


class UserDetailView(LoginRequiredMixin, View):
    form_class = UserForm
    template_name = 'account/edit_account.html'

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Profile')
        else:
            messages.error(request, 'Profile update request failed')
        return redirect(reverse('account:edit_profile'))


class MyLoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    next_page = reverse_lazy('dashboard:dashboard')


class MyLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'
    next_page = reverse_lazy('dashboard:info')


class MyPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'account/password_change_form.html'
    success_url = reverse_lazy('account:password_change_done')


class MyPasswordChageDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


class MyPasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')


class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
