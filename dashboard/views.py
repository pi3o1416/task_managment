
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

# Create your views here.


class Dashboard(LoginRequiredMixin, View):
    template_name = 'pages/dashboard.html'

    def get(self, request, format=None):
        return render(request, self.template_name)


class Info(View):
    template_name = 'pages/info.html'

    def get(self, request):
        return render(request, self.template_name, {})
