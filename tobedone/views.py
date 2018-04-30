from django.shortcuts import render, redirect

from .models import Tobedone
from .forms import TodoForm
import socket

# Create your views here.
def index(request):
	todo_list = Tobedone.objects.filter(ip_address = socket.gethostbyname(socket.getfqdn())).order_by('id')
	form = TodoForm()
	context = {'todo_list' : todo_list, 'form' : form}
	return render(request, 'tobedone/index.html', context)

def addTodo(request):
	form = TodoForm(request.POST)
	if form.is_valid():
		new_todo = Tobedone(text = request.POST['text'], ip_address = socket.gethostbyname(socket.getfqdn()))
		new_todo.save()
	return redirect('index')

def completeTodo(request, todo_id):
	todo = Tobedone.objects.get(pk = todo_id)
	todo.complete = True
	todo.save()
	return redirect('index')

def deleteCompleted(request):
	Tobedone.objects.filter(complete__exact = True).filter(ip_address = socket.gethostbyname(socket.getfqdn())).delete()
	return redirect('index')

def deleteall(request):
	Tobedone.objects.filter(ip_address = socket.gethostbyname(socket.getfqdn())).delete()
	return redirect('index')