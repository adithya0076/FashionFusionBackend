from rest_framework import viewsets, status
from rest_framework.response import Response
from api import models as model
from api import serializer as ser
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class BaseView:
    create_msg = 'data created'
    retreive_msg = 'data retreived'
    update_msg = 'data updated'
    delete_msg = 'data deleted'

class ItemViewSet(viewsets.ModelViewSet, BaseView):
    queryset = model.Item.objects.all()
    serializer_class = ser.ItemSerializer
    ordering = ['-id']
    search_fields = ['name']

    def get_queryset(self):
        return self.queryset.order_by('-id')
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        category = request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            'success': True,
            'message': 'Data retrieved successfully'
        }, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

