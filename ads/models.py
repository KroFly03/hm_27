from django.db import models
from marshmallow import Schema, fields


class Ads(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    price = models.IntegerField()
    description = models.CharField(max_length=600)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()


class AdsSchema(Schema):
    name = fields.String()
    author = fields.String()
    price = fields.Integer()
    description = fields.String()
    address = fields.String()
    is_published = fields.Boolean()
