from django.db import models

# Create your models here.
class Oven(models.Model):
    o_num = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.o_num)


class Temp(models.Model):
    date = models.DateField()
    time = models.TimeField()
    cyclic_hours = models.DurationField()
    temperature = models.FloatField()
    oven = models.ForeignKey(Oven, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{str(self.temperature)} of {str(self.oven)} at {str(self.time)}'


