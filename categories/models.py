from django.db import models
from marshmallow import Schema, fields


class Category(models.Model):
    name = models.CharField(max_length=100)


class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String()
