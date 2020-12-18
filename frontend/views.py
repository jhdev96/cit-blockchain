from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    return redirect("index")

  else:
    context = {
      'user': request.user
    }

    return render(request, 'partials/_login.html', context)

def logout_user(request):
  logout(request)
  return redirect('index')

@login_required(login_url='/')
def blocks(request):
  context = {
    'blocks': Block.objects.order_by('-timestamp')
  }
  
  return render(request, 'partials/_blocks.html', context)

@login_required(login_url='/')
def students(request):
  context = {
    'students': StudentRecord.objects.order_by('id')
  }

  return render(request, 'partials/_students.html', context)

@login_required(login_url='/')
def student_detail(request, id):

  student = StudentRecord.objects.get(id=id)
  
  context = {
    'student': student
  }

  return render(request, 'partials/_student_detail.html', context)
