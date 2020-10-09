from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentRecord 
from blockchain_records.models import Block


def index(request):
  return HttpResponse('<h1>Index</h1>')


def add_record(request):
  if request.method == 'POST':
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    address = request.POST['address']
    email = request.POST['email']
    phone = request.POST['phone']
    dob = request.POST['dob']


    student = StudentRecord.objects.create(
      first_name = firstname,
      last_name = lastname,
      address = address,
      email = email,
      phone = phone,
      dob = dob,
      

    )
    if len(Block.objects.all()) ==0:
      
      
      block = Block(None, student, nonce=len(Block.objects.all())+1)
      block.save()
    else:
      previousblock = Block.objects.all()[-1]
      Block.objects.create(previousblock, student, nonce=len(Block.objects.all())+1)
  return redirect('index')

def delete_record(request):
  if request.method =='POST':
    record_id = request.POST['id']
    record = StudentRecord.objects.get(id=record_id)
    previousblock = Block.objects.all()[-1]
    block = Block.objects.create(previousblock, record,nonce=len(Block.objects.all())+1)
    record.delete()
  return redirect('index')








  
