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


class ComputerPageView(TemplateView):
    template_name = 'shop_example/computer_page.html'

    def get_context_data(self, **kwargs):
        computer_to_render = Computers.objects.get(id=self.kwargs['id'])
        context = super().get_context_data(**kwargs)
        context.update({
            'computer_to_render': computer_to_render,

        })
        return context
