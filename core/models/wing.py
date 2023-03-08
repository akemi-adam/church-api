from django.db import models

class Wing(models.Model):
    
    wing = models.CharField(max_length = 100, verbose_name = 'Wing')

    church = models.ForeignKey('core.Church', on_delete = models.CASCADE, verbose_name = 'Church')

    users = models.ManyToManyField('core.User', through = 'Due')

    def __str__(self) -> str:
        return f'{self.wing} - {self.church.denomination}'