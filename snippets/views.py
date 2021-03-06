from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def tictactoe(request):
    return render(request, 'snippets/tictactoe.html', {})

def user_list(request):
    return render(request, 'snippets/base.html', {'div_id': 'user-list'})

def user_detail(request, pk=None):
    if not User.objects.filter(pk=pk).exists():
        raise Http404()

    return render(request, 'snippets/base.html', {'div_id': 'user-detail'})

def snippet_list(request):
    return render(request, 'snippets/base.html', {'div_id': 'snippet-list'})

def snippet_detail(request, pk=None):
    if not User.objects.filter(pk=pk).exists():
        raise Http404()

    return render(request, 'snippets/base.html', {'div_id': 'snippet-detail'})

def snippet_create(request):
    return render(request, 'snippets/base.html', {'div_id': 'snippet-create'})

def snippet_edit(request, pk=None):
    if not User.objects.filter(pk=pk).exists():
        raise Http404()

    return render(request, 'snippets/base.html', {'div_id': 'snippet-edit'})