from django.contrib import admin
from apps.parking.models import AutoCard
from .models import Inventorization

# Register your models here.


class MembershipInline(admin.TabularInline):
    model = Inventorization.inventoriztion.through


class InventorizationAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline
    ]
    exclude = ('inventoriztion',)


class AutoCardAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline
    ]

admin.site.register(Inventorization, InventorizationAdmin)
