from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tagler')
        tags = tag.split(' ')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        n = Note(title=title, content=content)
        n.save()
        for t in tags:
            tag_list = Tag.objects.all()
            tem = False
            for tag in tag_list:
                if(t == tag.name):
                    tag.notes.add(n)
                    tem = True
                    break
            if tem == True:
                break
            tag = Tag(name = t)
            tag.save()
            tag.notes.add(n)
        tag_list = Tag.objects.all()
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

def tags(request):
    if request.method == 'GET':
        all_tags = Tag.objects.all()
        return render(request, 'notes/tags.html', {'tags': all_tags})

def note_list(request, index):
    tag = Tag.objects.get(id=index)
    return render(request, 'notes/note_list.html', {'notes': tag.notes.all()})