import instance as instance
from rest_framework import serializers
from task4 import Profile
from rest_framework.response import Response


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('__all__', )

    def create(self, validated_data):
        user = self.context.get('request').user
        text = Profile.objects.create(owner=user, **validated_data)
        return text

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_seeializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        partial = partial
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response()