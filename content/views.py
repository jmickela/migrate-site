from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework import serializers

from .models import NewsItem, PressRelease, OtherContent


class ContentSerializer(serializers.ModelSerializer):
	new_url = serializers.SerializerMethodField()
	class Meta:
		model = NewsItem

	def get_new_url(self, item):
		return item.get_new_url()


class NewsList(ListAPIView):
	queryset = NewsItem.objects.all()
	serializer_class = ContentSerializer


class PressList(ListAPIView):
	queryset = PressRelease.objects.all()
	serializer_class = ContentSerializer

class ChemicalsList(ListAPIView):
	queryset = OtherContent.objects.filter(do_import=True, content_type=OtherContent.CHEMICAL)
	serializer_class = ContentSerializer

class OtherContentList(ListAPIView):
	queryset = OtherContent.objects.filter(do_import=True, content_type=OtherContent.PAGE)
	serializer_class = ContentSerializer


class ActionAlertList(ListAPIView):
	queryset = OtherContent.objects.filter(do_import=True, content_type=OtherContent.ACTION_ALERT)
	serializer_class = ContentSerializer


class ReportList(ListAPIView):
	queryset = OtherContent.objects.filter(do_import=True, content_type=OtherContent.REPORT)
	serializer_class = ContentSerializer