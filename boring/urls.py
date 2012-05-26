from django.conf.urls import patterns, include, url

from django.views.generic import ListView, DetailView
from .models import Entry

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Entry), name="boring.entry_list"),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Entry), name="boring.entry_detail"),
)
