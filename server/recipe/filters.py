from recipe.models import Recipe
from django_filters import rest_framework as filters


class RecipeFilter(filters.FilterSet):
    from_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    to_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")
    rating = filters.NumberFilter(field_name="rating", lookup_expr="gte")
    duration = filters.NumberFilter(field_name="duration", lookup_expr="lte")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    creator = filters.CharFilter(field_name="creator")
    category = filters.CharFilter(method="filter_category")

    class Meta:
        model = Recipe
        fields = (
            "name",
            "rating",
            "from_date",
            "to_date",
            "creator",
            "category",
            "duration",
        )

    def filter_category(self, qs, name, value):
        category_list = self.request.query_params.getlist("category", "")
        final_filtered_query = qs
        for category in category_list:
            final_filtered_query = final_filtered_query.filter(
                categories__id__contains=category
            )
        return final_filtered_query
