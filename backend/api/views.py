from django.shortcuts import render
from rest_framework import generics
from .models import Transaction
from .models import Transaction
from .serializres import TransactionSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class= TransactionSerializer

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Transaction.objects.all()
     serializer_class= TransactionSerializer
     lookup_field = "id"
