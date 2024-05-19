from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets
from api.models import Company,Employee
# from django.contrib.auth.models import company
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
API_KEY = 'd0b69496c18e463f888a273cb521ea9f'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    


def home(request):
    country = request.GET.get('country')
    # url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    url = f'https://newsapi.org/v2/top-headlines?country=in&apikey=d0b69496c18e463f888a273cb521ea9f'

    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {

        'articles' : articles ,
    }

    return render(request, 'api/home.html',context)