from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tagler')
        tags = tag.split(' ')
        print(tags)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        n = Note(title=title, content=content)
        n.save()
        for t in tags:
            print(f"****{t}****")
            tag_list = Tag.objects.all()
            if tag_list.count() != 0:
                existe = False
                for tag in tag_list:
                    if(t == tag.name):
                        print(f'{t} == {tag.name}, {n}')
                        tag.notes.add(n)
                        existe = True
                        break
                if not existe:
                    print(f'{t} != all tag names')
                    tag = Tag(name = t)
                    tag.save()
                    tag.notes.add(n)
            else:
                print(f'nota: {n}')
                tag = Tag(name = t)
                tag.save()
                tag.notes.add(n)
        n.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, index):
    Note.objects.get(id=index).delete()
    tag_list = Tag.objects.all()
    for tag in tag_list:
            if(tag.notes.count() == 0):
                tag.delete()
    return redirect('index')

def edit(request, index):
    if request.method == 'POST':
        n = Note.objects.get(id=index)
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tags')
        tags = tag.split(' ')
        tag_list = Tag.objects.all()
        for tag_in in n.tag_set.all():
            tag_in.notes.remove(n)
        for t in tags:
            print(f"****{t}****")
            if tag_list.count() != 0:
                existe = False
                for tag in tag_list:
                    if(t == tag.name):
                        print(f'{t} == {tag.name}')
                        tag.notes.add(n)
                        existe = True
                        break
                if not existe:
                    print(f'{t} != all tag names')
                    tag = Tag(name = t)
                    tag.save()
                    tag.notes.add(n)
            else:
                print(f'nota: {n}')
                tag = Tag(name = t)
                tag.save()
                tag.notes.add(n)
        for tag in tag_list:
            if(tag.notes.count() == 0):
                tag.delete()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
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