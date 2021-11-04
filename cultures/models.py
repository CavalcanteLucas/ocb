from django.db import models


class Culture(models.Model):
    class Origins(models.TextChoices):
        SEED = 'seed', 'Seed'
        CLONE = 'clone', 'Clone'

    class Rooms(models.TextChoices):
        CLONING = 'cloning', 'Cloning'
        VEGETATION = 'vegetation', 'Vegetation'
        FLOWERING = 'flowering', 'Flowering'
        DRYING = 'drying', 'Drying'
        STORAGE = 'storage', 'Storage'

    class DiscardReasons(models.TextChoices):
        MALE = 'male', 'Male'
        PEST = 'pest', 'Pest'

    genetic_name = models.CharField('Genetic name', max_length=200)
    origin = models.CharField(
        'Origin', max_length=20, choices=Origins.choices, default=Origins.SEED
    )
    start_date = models.DateField()
    flowering_date = models.DateField(null=True, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    harvest_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    drying_date = models.DateField(null=True, blank=True)
    drying_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    storage_date = models.DateField(null=True, blank=True)
    discarded = models.BooleanField(default=False)
    discard_reason = models.CharField(
        'Discard Reason', max_length=4, choices=DiscardReasons.choices, null=True, blank=True
    )

    def __str__(self):
        return self.genetic_name
