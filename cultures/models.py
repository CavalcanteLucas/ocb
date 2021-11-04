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

            # Ensure dates are filled in at the correct order

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

        # Ensure the chronological order of dates

        if (
            self.flowering_date
            and self.start_date
            and self.flowering_date <= self.start_date
        ):
            raise ValidationError(
                {
                    'flowering_date': ValidationError(
                        _(
                            'The flowering date must be later than the start date.'
                        )
                    )
                }
            )

        if (
            self.harvest_date
            and self.flowering_date
            and self.harvest_date <= self.flowering_date
        ):
            raise ValidationError(
                {
                    'harvest_date': ValidationError(
                        _(
                            'The harvest date must be later than the flowering date.'
                        )
                    )
                }
            )

        if (
            self.drying_date
            and self.harvest_date
            and self.drying_date <= self.harvest_date
        ):
            raise ValidationError(
                {
                    'harvest_date': ValidationError(
                        _(
                            'The drying date must be later than the harvest date.'
                        )
                    )
                }
            )

        if (
            self.storage_date
            and self.drying_date
            and self.storage_date <= self.drying_date
        ):
            raise ValidationError(
                {
                    'harvest_date': ValidationError(
                        _(
                            'The storage date must be later than the drying date.'
                        )
                    )
                }
            )
