# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HomeForm
from .models import Risk

class HomeView(TemplateView):
    template_name = 'accounts/index.html'

    def get(self, request):
        the_form = HomeForm()
        context = {
            "title": "Insurance Form",
            "form" : the_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form = HomeForm()

            # print('*'*50)
            # print(request.POST)
            # print('*'*50)

            return HttpResponse('Submitted')
        else:
            return HttpResponse('Failed')
