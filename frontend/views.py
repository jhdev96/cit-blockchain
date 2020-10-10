from django.shortcuts import render
from django.http import HttpResponse
from blockchain_records.models import Block
from student_records.models import StudentRecord


def index(request):
  context = {
    'blocks': Block.objects.order_by('-timestamp')
  }
  
  return render(request, 'partials/_blocks.html', context)

def students(request):
  context = {
    'students': StudentRecord.objects.all()
  }

  return render(request, 'partials/_students.html', context)

def student_detail(request, id):

  student = StudentRecord.objects.get(id=id)
  print(student.first_name, student.last_name)

  return HttpResponse('<h1>Student detail</h1>')
