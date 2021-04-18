from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarSpecs, CarPlan
from .serializers import CarSpecsSerializer, CarPlanSerializer, SameCarCheckSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action


class CarSpecsViewSet(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        q = CarSpecs.objects.all()
        return q

    def retrieve(self, request, *args, **kwargs):
        params = kwargs['pk']
        query_list = params.split('-')
        try:
            pk = int(query_list[0])
            is_numeric = True
        except ValueError:
            is_numeric = False

        if is_numeric:
            car_specs = CarSpecs.objects.filter(pk=query_list[0])
            serializer = CarSpecsSerializer(car_specs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if len(query_list) > 1:
            car_specs = CarSpecs.objects.filter(
                car_brand=query_list[0], production_year=query_list[1])
        else:
            car_specs = CarSpecs.objects.filter(car_brand=query_list[0])
        serializer = CarSpecsSerializer(car_specs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        exist_in_db = False
        car_data = request.data
        for car in CarSpecs.objects.all():
            serializer = SameCarCheckSerializer(car)
            if car_data == serializer.data:
                exist_in_db = True

        serializer = CarSpecsSerializer(data=car_data, many=False)
        if serializer.is_valid() and not exist_in_db:
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        car = self.get_object()
        car.delete()

        return Response('Deleted..', status=status.HTTP_204_NO_CONTENT)
