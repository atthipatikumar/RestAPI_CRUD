from rest_framework import serializers
from .models import Details

class DetailSerializers(serializers.Serializer):
    Name = serializers.CharField(max_length=200)
    Address = serializers.CharField(max_length=250)
    Profile_Picture = serializers.ImageField()
    Birthdate = serializers.DateField()
    Years_of_experience = serializers.IntegerField()
    Preferred_Language = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Details.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Address = validated_data.get('Address', instance.Address)
        instance.Profile_Picture = validated_data.get('Profile_Picture', instance.Profile_Picture)
        instance.Birthdate = validated_data.get('Birthdate', instance.Birthdate)
        instance.Years_of_experience = validated_data.get('Years_of_experience', instance.Years_of_experience)
        instance.Preferred_Language = validated_data.get('Preferred_Language', instance.Preferred_Language)
        instance.user_id = validated_data.get('user_id', instance.user_id)

        instance.save()
        return instance