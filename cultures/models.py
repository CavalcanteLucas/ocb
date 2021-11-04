from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
    harvest_weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    drying_date = models.DateField(null=True, blank=True)
    drying_weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    storage_date = models.DateField(null=True, blank=True)
    discarded = models.BooleanField(default=False)
    discard_reason = models.CharField(
        'Discard Reason',
        max_length=4,
        choices=DiscardReasons.choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.genetic_name

    def clean(self):
        if self.discard_reason is not None and not self.discarded:
            raise ValidationError(
                {
                    'discard_reason': ValidationError(
                        _(
                            'Discard the sample before assigning a discard reason.'
                        )
                    )
                }
            )

        if self.harvest_date is not None and self.flowering_date is None:
            raise ValidationError(
                {
                    'harvest_date': ValidationError(
                        _(
                            'The sample must have a flowering date before being harvested.'
                        )
                    )
                }
            )

        if self.drying_date is not None and self.harvest_date is None:
            raise ValidationError(
                {
                    'drying_date': ValidationError(
                        _(
                            'The sample must have a harvest date before being dried.'
                        )
                    )
                }
            )

        if self.storage_date is not None and self.drying_date is None:
            raise ValidationError(
                {
                    'storage_date': ValidationError(
                        _(
                            'The sample must have a drying date before being storaged.'
                        )
                    )
                }
            )
