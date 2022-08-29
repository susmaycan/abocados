
from meal.models import Meal
from django_filters import rest_framework as filters


class MealFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    to_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    date = filters.DateFilter(field_name='date', lookup_expr='contains')

    class Meta:
        model = Meal
        fields = (
            'from_date',
            'to_date',
            'date',
        )
