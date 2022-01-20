from django.db import models

class Card(models.Model):
    name = models.CharField('Card Name', max_length=5)

    def __str__(self):
        return self.name