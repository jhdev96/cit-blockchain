from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import StudentRecord 
from blockchain_records.models import Block


def get_student_fields(request) -> dict:
  student_fields = dict(first_name=request.POST['firstname'],
                        last_name=request.POST['lastname'],
                        address=request.POST['address'],
                        email=request.POST['email'],
                        phone=request.POST['phone'],
                        dob=request.POST['dob'],
                        time_pref=request.POST['time-pref'],
                        empl_status=request.POST['empl-status'],
                        problem_solving=request.POST['prob-solving'],
                        data_bg=request.POST['data-bg'],
                        mean_med_mode=request.POST['mean-med-mode'],
                        programming_exp=request.POST['programming-exp'],
                        sql_exp=request.POST['sql-exp'],
                        job_goal=request.POST['job-goal'],
                        events=request.POST['events'],
                        commitments=request.POST['commits'],
                        other=request.POST['other'],
                        how_find_codeit=request.POST['how-find-codeit'],
                        has_laptop=request.POST['has-laptop'],
                        operating_sys=request.POST['op-sys'],
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

  return redirect('transactions')

@login_required(login_url='/')
def update_record(request):
  if request.method =='POST':
    record_id = request.POST['id']
    student_bio = request.POST['bio']
    student_fields = get_student_fields(request)
    student_fields['bio'] = student_bio

    # get and update the record fields
    record_qs = StudentRecord.objects.filter(id=record_id)
    record_qs.update(**student_fields)

    block_queryset = Block.objects.all()
    previous_block = Block.objects.order_by('-timestamp')[0]

    Block.objects.create(
      previous_block=previous_block, 
      action="Update",
      data=record_qs[0],
      nonce=len(block_queryset)
    )

  return redirect('student', id=record_id)

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

  return redirect('transactions')








  
