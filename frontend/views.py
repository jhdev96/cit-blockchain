from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from blockchain_records.models import Block
from student_records.models import StudentRecord


def index(request):

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(
            request, 
            username=username, 
            password=password
           )
    if user is not None:
      login(request, user)
      return redirect('transactions')

  else:
    context = {
      'user': request.user
    }

    return render(request, 'partials/_login.html', context)

def logout_user(request):
  logout(request)
  return redirect('index')

def blocks(request):
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
