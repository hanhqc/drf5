from rest_framework.serializers import ModelSerializer

from app1.models import Computer


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = ("computer_name", "price", "brand")
