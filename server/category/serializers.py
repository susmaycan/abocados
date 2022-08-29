from django.forms import ValidationError
from rest_framework import serializers
from category.constants import CategoryTypes
from .models import Category
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "description", "picture", "type")
        read_only_fields = ("id",)

    def get_type(self, instance):
        # TODO get also name
        return instance.type


class CategorySelectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class CategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=180,
        required=True,
        validators=[UniqueValidator(queryset=Category.objects.all())],
    )
    description = serializers.CharField(max_length=1000, required=False)
    picture = serializers.FileField(required=False)
    type = serializers.CharField(required=True, max_length=1)

    def validate_type(self, value):
        if value not in CategoryTypes:
            raise ValidationError("type %s doesn't exist" % (value))
        return value

    def create(self, data):
        category = Category.objects.create(**data)
        return category
