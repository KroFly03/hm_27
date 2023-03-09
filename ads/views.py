import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, AdsSchema


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()

        ads_schema = AdsSchema(many=True)
        response = ads_schema.dump(ads)

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_schema = AdsSchema()

        data = ads_schema.loads(request.body)

        ads = Ads.objects.create(**data)

        response = ads_schema.dump(ads)

        return JsonResponse(response)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ads_schema = AdsSchema()

            ads = self.get_object()

            response = ads_schema.dump(ads)

            return JsonResponse(response)

        except Ads.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
