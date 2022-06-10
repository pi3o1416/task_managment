
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from .models import Connection

# Create your views here.
User = get_user_model()
PENDING = 'PEN'
ACCEPTED = 'ACC'
BLOCKED = 'BLC'


class RequestConnection(LoginRequiredMixin, View):
    template_name = 'connection/connection_request.html'

    def post(self, request):
        request_from = request.user
        request_to = self.get_object(request.POST['username'])
        connection = Connection(
            connected_from=request_from,
            connected_to=request_to,
            connection_status='PEN'
        )
        connection.save()
        return render(request, self.template_name, {'user': request_to})

    def get_object(self, username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise Http404


class ConfirmConnection(LoginRequiredMixin, View):
    template_name = 'connection/confirm_connection.html'

    def post(self, request):
        connection = self.get_object(request.POST['connection_request_id'])
        connected_from = connection.connected_from
        connected_to = connection.connected_to
        connection.connection_status = ACCEPTED
        connection.save()
        # whole connection is like a undirected graph
        reverse_connection = Connection(
            connected_from=connected_to, connected_to=connected_from, connection_status=ACCEPTED)
        reverse_connection.save()
        return render(request, self.template_name, {'connected_user': connected_from})

    def get_object(self, connection_id):
        try:
            connection = Connection.objects.get(id=connection_id)
            return connection
        except Connection.DoesNotExist:
            raise Http404


class ConnectionList(View):
    template_name = 'connection/connection_list.html'

    def get(self, request):
        connections = self.get_queryset(request.user)
        return render(request, self.template_name, {'connections': connections})

    def get_queryset(self, user):
        connections = user.connected_to.filter(connection_status=ACCEPTED)
        return connections


class RequestList(LoginRequiredMixin, View):
    template_name = 'connection/connection_request_list.html'

    def get(self, request):
        connection_requests = self.get_queryset(request.user)
        return render(request, self.template_name, {'connection_requests': connection_requests})

    def get_queryset(self, user):
        condition1 = Q(connected_to=user)
        condition2 = Q(connection_status=PENDING)
        connection_requests = Connection.objects.filter(
            condition1 & condition2)
        return connection_requests


class SearchUser(LoginRequiredMixin, View):
    template_name = 'connection/search.html'
    context = dict()

    def get(self, request):
        keyword = request.GET['search']
        user = request.user
        self.context['peoples'] = self.get_queryset(keyword, user)
        self.context['keyword'] = keyword
        self.context['connections'] = self.get_connections_by_status(
            user.connected_to)
        self.context['pending_connections'] = self.get_connections_by_status(
            user.connected_to, status=PENDING)
        self.context['connection_requests'] = self.get_connections_by_status(
            user.connected_from, status=PENDING, column_name='connected_from')
        return render(request, self.template_name, self.context)

    def get_queryset(self, keyword, user):
        condition1 = Q(username__icontains=keyword)
        condition2 = Q(username=user.username)
        users = User.objects.filter(condition1 & ~condition2)
        return users

    def get_connections_by_status(self, user_relation, status=ACCEPTED, column_name='connected_to'):
        """
        user_relation indicate either connected_to or connected_from
        """
        connections = user_relation.filter(
            connection_status=status).values_list(column_name, flat=True)
        return connections
