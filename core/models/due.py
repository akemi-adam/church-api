from django.db import models

class Due(models.Model):
    
    user = models.ForeignKey('core.User', on_delete = models.CASCADE, verbose_name = 'User')

    wing = models.ForeignKey('core.Wing', on_delete = models.CASCADE, verbose_name = 'Wing')

    offer = models.DecimalField(max_digits = 6, decimal_places = 2, verbose_name = 'Offer')

    def __str__(self) -> str:
        return f'{self.username} from the {self.wing.wing} ward made an offer of {self.offer}'