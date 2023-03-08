from django.db import models

class Church(models.Model):
    
    denomination = models.CharField(max_length = 100, verbose_name = 'Denomination')

    def __str__(self) -> str:
        return f'{self.denomination}'

