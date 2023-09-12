from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        n = Note(title=title, content=content)
        n.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, index):
    Note.objects.get(id=index).delete()
    return redirect('index')

def edit(request, index):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        n = Note.objects.get(id=index)
        if(title == '' and content == ''):
            print('entrou aqui all')
            n.title = n.title
            n.content = n.content
        elif(title == ''):
            print('entrou aqui title')
            n.title = n.title
            n.content = content
        elif(content == ''):
            print('entrou aqui content')
            n.title = title
            n.content = n.content
        else:
            n.title = title
            n.content = content
        n.save()
        return redirect('index')
    else:
        note = Note.objects.get(id=index)
        return render(request, 'notes/edit.html', {'note': note})