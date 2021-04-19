from rest_framework import serializers
from .models import CarSpecs, CarPlan


class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = '__all__'


class CarPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPlan
        fields = '__all__'

class SameCarCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['car_brand','car_model','production_year','car_body','engine_type']