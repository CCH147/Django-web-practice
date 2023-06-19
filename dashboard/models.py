from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length= 255)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = '國家 人口 Data'

    def __str__(self):
        return f'{self.country}-{self.population}'

class City(models.Model):
    name = models.CharField(max_length = 255, blank=True, null=True)
    def __str__(self):
            return self.name


class County(models.Model):
    city =  models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
            return self.name