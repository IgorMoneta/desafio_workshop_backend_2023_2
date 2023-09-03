from django.db import models


class Time(models.Model):
    times = models.CharField(null= False, max_length = 40)

    def __str__(self):
        return f'Time: {self.time}'
    
class Caracteristicas(models.Model):
    estadio = models.CharField(null= False , max_length = 40)
    cidade = models.CharField( null = False , max_length = 40)
    times = models.ForeignKey(
    Time,
    max_length=20,
    on_delete=models.CASCADE
    )




    
    
