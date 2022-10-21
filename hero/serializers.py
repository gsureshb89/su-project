from rest_framework import serializers
from hero.models import Hero

class HeroSerializer(serializers.ModelSerializer):
	""""""
	class Meta:
		model = Hero
		fields = ['unique_id', 'first_name', 'last_name']