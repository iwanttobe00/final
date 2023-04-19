from django.utils import timezone
from rest_framework.exceptions import ValidationError


def year_validator(year):
    if year > timezone.now().year:
        raise ValidationError(f'{year} - некорректный год')
