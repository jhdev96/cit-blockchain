from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import StudentRecord 
from blockchain_records.models import Block


def index(request):
  return HttpResponse('<h1>Index</h1>')

def get_student_fields(request) -> dict:
  student_fields = dict(first_name=request.POST['firstname'],
                        last_name=request.POST['lastname'],
                        address=request.POST['address'],
                        email=request.POST['email'],
                        phone=request.POST['phone'],
                        dob=request.POST['dob']
                       )
  return student_fields

@login_required(login_url='/')
def add_record(request):
  if request.method == 'POST':
    student_fields = get_student_fields(request)

    student = StudentRecord.objects.create(
                **student_fields
              )

    block_qs = Block.objects.all()

    previous_block = None
    if len(block_qs) > 0:
      previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
        previous_block=previous_block, 
        action="Add",
        data=student, 
        nonce=len(block_qs)
      )

  return redirect('index')

@login_required(login_url='/')
def update_record(request):
  if request.method =='POST':
    record_id = request.POST['id']
    student_fields = get_student_fields(request)
    print(record_id, student_fields)


    # get and update the record fields
    record_qs = StudentRecord.objects.filter(id=record_id)
    record_qs.update(**student_fields)
    print(record_qs)

    block_queryset = Block.objects.all()
    previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
      previous_block=previous_block, 
      action="Update",
      data=record_qs[0],
      nonce=len(block_queryset)
    )

  return redirect('index')

@login_required(login_url='/')
def delete_record(request):
  if request.method =='POST':
    record_id = request.POST['id']
    record = StudentRecord.objects.get(id=record_id)

    block_queryset = Block.objects.all()
    previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
      previous_block=previous_block, 
      action="Remove",
      data=record,
      nonce=block_queryset
    )
    record.delete()

  return redirect('index')








  
