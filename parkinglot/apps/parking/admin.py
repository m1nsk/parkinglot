from .models import CarOwner, CarColor, CarModel, AutoCard, Entry
from django.contrib import admin

# Register your models here.


class EntryInline(admin.ModelAdmin):
    model = Entry


class AutoCardInline(admin.ModelAdmin):
    model = AutoCard


class CarModelInline(admin.StackedInline):
    inlines = [
        AutoCardInline
    ]


class CarColorInline(admin.StackedInline):
    inlines = [
        AutoCardInline
    ]


class CarOwnerInline(admin.StackedInline):
    inlines = [
        AutoCardInline,
        EntryInline
    ]


admin.site.register(CarColor)
admin.site.register(CarModel)
admin.site.register(CarOwner)
admin.site.register(Entry)
admin.site.register(AutoCard, AutoCardInline)