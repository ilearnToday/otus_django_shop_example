from django.views.generic import TemplateView
from .models import SiteMenu, Computers


class SiteMenuMixin:
    def get_context_data(self, **kwargs):
        menu_items = SiteMenu.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({
                'menu_items': menu_items,
        })
        return context


class MainPageView(SiteMenuMixin, TemplateView):
    template_name = 'shop_example/main_page.html'

    def get(self, request, *args, **kwargs):
        computers = Computers.objects.all()
        context = super().get_context_data(**kwargs)
        context.update({
            'computers': computers
        })
        return self.render_to_response(context)


class ComputerPageView(TemplateView):
    template_name = 'shop_example/computer_page.html'

    def get_context_data(self, **kwargs):
        computer_to_render = Computers.objects.get(id=self.kwargs['id'])
        context = super().get_context_data(**kwargs)
        context.update({
            'computer_to_render': computer_to_render,

        })
        return context
