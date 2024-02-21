from django.contrib import admin
from .models import PointOfInterest, Rating
from django.db.models import Avg


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1


class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = (
        "poi_id",
        "poi_name",
        "poi_external_id",
        "poi_category",
        "average_rating",
    )
    search_fields = ("poi_id", "poi_external_id")
    list_filter = ("poi_category",)
    inlines = [RatingInline]

    def average_rating(self, obj):
        avg_rating = obj.ratings.aggregate(Avg('score'))['score__avg']
        return round(avg_rating, 2) if avg_rating is not None else None

    average_rating.short_description = "Avg. Rating"


admin.site.register(PointOfInterest, PointOfInterestAdmin)
