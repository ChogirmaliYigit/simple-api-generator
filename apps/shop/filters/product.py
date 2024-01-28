from rest_framework import filters


class ProductFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_mappings = {
            "priceFrom": "price__gte",
            "priceTo": "price__lte",
            "discountPercentageFrom": "discount_percentage__gte",
            "discountPercentageTo": "discount_percentage__lte",
            "ratingFrom": "rating__gte",
            "ratingTo": "rating__lte",
        }

        filters_dict = {
            filter_mappings[param]: request.query_params[param]
            for param in filter_mappings
            if request.query_params.get(param)
        }

        return queryset.filter(**filters_dict)
