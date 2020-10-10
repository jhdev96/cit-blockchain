from django.shortcuts import render
from blockchain_records.models import Block


def index(request):
  context = {
    'blocks': Block.objects.order_by('-timestamp')
  }
  
  return render(request, 'index.html', context)
