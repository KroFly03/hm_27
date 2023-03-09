import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from categories.models import Category, CategorySchema


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        category_schema = CategorySchema(many=True)
        response = category_schema.dump(categories)

        return JsonResponse(response, safe=False)

    def post(self, request):
        category_schema = CategorySchema()

        data = category_schema.loads(request.body)

        category = Category.objects.create(**data)

        response = category_schema.dump(category)

        return JsonResponse(response)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category_schema = CategorySchema()

            category = self.get_object()

            response = category_schema.dump(category)

            return JsonResponse(response)

        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
