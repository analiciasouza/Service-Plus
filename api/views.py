from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models.profissional import Profissional
from api.serializers.profissional import ProfissionalSerializer

@api_view(['GET', 'POST'])
def profissional_view(request):
    if request.method == 'GET':
        """List all models."""
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        """Create a new model instance."""
        serializer = ProfissionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def profissional_detail(request, pk):
    """Retrieve, update, or delete a model instance."""
    try:
        profissional = Profissional.objects.get(pk=pk)
    except Profissional.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfissionalSerializer(profissional)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfissionalSerializer(profissional, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        profissional.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)