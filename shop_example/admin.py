from django.contrib import admin

from .models import SiteMenu, Computers


@admin.register(SiteMenu)
class SiteMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu_item_name', ]


@admin.register(Computers)
class ComputersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',
                    'picture_link', 'comp_link',
                    'comp_price', 'price_currency',
                    'display_type', 'processor_type',
                    'ram_type', 'ssd_volume',
                    ]