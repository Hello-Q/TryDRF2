from rest_framework import serializers
from .models import *

#
# class PublisherSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         return Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         instance:实例， 原数据实例
#         validated_data: 验证过的数据，前台传来的
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.name)
#         instance.save()
#         return instance
# #


class PublisherSerializer(serializers.ModelSerializer):
    # operator = serializers.ReadOnlyField(source="operator.username")
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'address',
        )
        # fields = "__all__"


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'publisher',
        )
