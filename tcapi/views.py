from django.shortcuts import render
from django.views.generic import TemplateView
from os.path import exists


class PageView(TemplateView):
    """
    TODO: Documentation
    """
    def get_template_names(self):
        template_name = self.kwargs.get('template', 'status.html')
        if not exists('template/' + template_name):
            template_name = 'missing.html'
        return template_name
