from django.db import models
from model_utils import Choices


class Question(models.Model):
    CAN_OPTION = Choices('papier', 'metale_plastik', 'szko', 'bio', 'zmieszane')
    content = models.CharField(max_length=30)
    answer = models.CharField(choices=CAN_OPTION, max_length=20)

    def __str__(self):
        return self.content
