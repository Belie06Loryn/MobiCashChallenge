# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AddForm
from .models import Add
from django.contrib.auth.models import User
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AddSerializer
from rest_framework import status

@login_required(login_url='/accounts/login/')
def page(request):
    # response = requests.get('http://dev.mobivat.com:8080/vsdc_module/mobivat/api/product/')
    # geodata = response.json()
    return render(request,'all-files/index.html',
    {
# 'sku': geodata['sku'],
# 'upc': geodata['upc'],
# 'pname': geodata['pname'],
# 'description': geodata['description'],
# 'taxcode': geodata['taxcode'],
# 'tax_rate': geodata['tax_rate'],
# 'unitp': geodata['unitp'],
# 'quantity': geodata['quantity'],
# 'tax_percent': geodata['tax_percent']
})

@login_required(login_url='/accounts/login/')
def add_customer(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('add_customer')

    else:
        form = AddForm()
    return render(request, 'all-files/add_customer.html', {'form': form})    

@login_required(login_url='/accounts/login/')
def view_customer(request):
    customers = Add.objects.all()
    return render(request,'all-files/view_customer.html',{'customers':customers})    

@login_required(login_url='/accounts/login/')
def delete_customer(request):
    customers = Add.objects.all()
    return render(request,'all-files/delete_customer.html',{'customers':customers}) 

def dele(request,pk=None):
    object = Add.objects.get(id=pk)   
    object.delete()
    return render(request,'all-files/delete_customer.html')

def update(request,pk=None):
    current_user = request.user
    if request.method == 'POST':
        if Add.objects.filter(id=pk).exists():
            form = AddForm(request.POST, request.FILES,instance=Add.objects.get(id=pk))
        else:
            form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('view_customer',pk.id)

    else:
        if Add.objects.filter(id=pk).exists():
            form = AddForm(instance = Add.objects.get(id=pk))
        else:
            form = AddForm()
    return render(request, 'all-files/add_customer.html', {'form': form})


@login_required(login_url='/accounts/login/')
def edit_customer(request):
    customers = Add.objects.all()
    return render(request,'all-files/edit_customer.html',{'customers':customers})


class AddList(APIView):
    def get(self,repuest, format=None):
        all_custo = Add.objects.all()
        serializers = AddSerializer(all_custo, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AddSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)    