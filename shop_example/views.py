from django.shortcuts import render

from django.views.generic import TemplateView
from .models import SiteMenu, Computers


class MainPageView(TemplateView):
    template_name = 'shop_example/main_page.html'

    def get_context_data(self, **kwargs):
        menu_items = SiteMenu.objects.all()
        computers = Computers.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({
                'menu_items': menu_items,
                'computers': computers,

        })
        return context
