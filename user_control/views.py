from django.template import loader
from django.http import HttpResponse
from .models import User, Task, TaskPhoto, TaskDocuments
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskDocumentForm


def main(request):
    template = loader.get_template('user_info.html')
    return HttpResponse(template.render())

def all_users(request):
  users = User.objects.all().values()
  tasks = Task.objects.all().values()
  photos = TaskPhoto.objects.all()
  template = loader.get_template('user_info.html')
  context = {
    'users': users,
    'tasks' : tasks,
    'photos' : photos,
  }
  return HttpResponse(template.render(context, request))


def upload_document(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Получаем задачу по ID
    if request.method == 'POST':
        form = TaskDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.task = task  # Связываем документ с задачей
            document.uploaded_by = request.user  # Указываем пользователя
            document.save()
            return redirect('task_detail', task_id=task.id)  # Перенаправляем на страницу задачи
    else:
        form = TaskDocumentForm()
    return render(request, 'upload_document.html', {'form': form, 'task': task})

