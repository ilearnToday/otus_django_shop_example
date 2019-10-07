from django.db import models


class SiteMenu(models.Model):

    menu_item_name = models.TextField()

    def __str__(self):
        return self.menu_item_name


class Computers(models.Model):

    class Meta:
        verbose_name = 'Computer'
        verbose_name_plural = 'Computers'

    name = models.TextField()
    picture_link = models.TextField(max_length=150)
    comp_link = models.ImageField()

    comp_price = models.DecimalField(decimal_places=1, max_digits=15)
    price_currency = models.CharField(max_length=1)
    display_type = models.TextField(max_length=200)
    processor_type = models.TextField(max_length=200)
    ram_type = models.TextField(max_length=150)
    ssd_volume = models.TextField(max_length=200)

