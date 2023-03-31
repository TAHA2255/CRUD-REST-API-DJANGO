from rest_framework import serializers
from .models import student
class studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    school = serializers.CharField(max_length=20)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.school = validated_data.get('school',instance.school)
        instance.age = validated_data.get('age',instance.age)
        instance.save()
        return instance
