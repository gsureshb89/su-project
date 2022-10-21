from django.contrib import admin
from hero.models import Hero
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
	pass

admin.site.register(Hero, HeroAdmin)