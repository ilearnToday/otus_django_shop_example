from django.db import models


class SiteMenu(models.Model):

    menu_item_name = models.TextField()

    def __str__(self):
        return '{}'.format(self.menu_item_name)


class Computers(models.Model):
    class Meta:
        verbose_name = 'Computer'
        verbose_name_plural = 'Computers'

    name = models.TextField()
    picture_link = models.TextField()


    def __str__(self):
        return ''
