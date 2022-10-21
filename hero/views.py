from hero.models import Hero
from hero.serializers import HeroSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HeroList(APIView):
	""""""
	def get(self, request, format=None):
		""""""
		hero_list = Hero.objects.all()
		hero_serializer = HeroSerializer(hero_list, many=True)
		return Response(hero_serializer.data)

	def post(self, request, format=None):
		""""""
		hero_serializer = HeroSerializer(data=request.data)
		if hero_serializer.is_valid():
			hero_serializer.save()
			return Response(hero_serializer.data, status=status.HTTP_201_CREATED)
		return Response(hero_serializer.error, status=status.HTTP_400_BAD_REQUEST)

class HeroDetails(APIView):
	""""""
	def get_object(self, pk):
		""""""
		try:
			return Hero.objects.get(unique_id=pk)
		except Hero.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		""""""
		hero_obj = self.get_object(pk)
		hero_serializer = HeroSerializer(hero_obj)
		return Response(hero_serializer.data)

	def put(self, request, pk, format=None):
		""""""
		hero_obj = self.get_object(pk)
		hero_serializer = HeroSerializer(hero_obj, data=request.data)
		if hero_serializer.is_valid():
			hero_serializer.save()
			return Response(hero_serializer.data)
		return Response(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		""""""
		hero_obj = self.get_object(pk)
		hero_obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)














