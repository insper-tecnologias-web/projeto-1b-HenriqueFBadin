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
        n = Note.objects.get(id=index)
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tags')
        print('*****{}*****'.format(tag))
        if ('\n' in tag):
            tags = tag.split('\n')
            for t in tags:
                tagIndex, newTag = t.split('->')
                i=0
                if n.tag_set.all().count() == 0 and newTag != '':
                    tag = Tag(name = newTag)
                    tag.save()
                    tag.notes.add(n)
                else:
                    for tag in n.tag_set.all():
                        existing_tag = Tag.objects.filter(name=newTag).first()
                        i+=1
                        if i == int(tagIndex):
                            print('index Igual')
                            if newTag == '':
                                print('entrou aqui', tag)
                                tag.delete()
                                tag.save()
                            else:
                                tag.name = newTag
                                tag.save()
                        elif not existing_tag:
                            tag = Tag(name = newTag)
                            tag.save()
                            tag.notes.add(n)

        else:
            tagIndex, newTag = tag.split('->')
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
        
        i=0
        for tag in n.tag_set.all():
            i+=1
            if i == int(tagIndex):
                if newTag == '':
                    tag.delete()
                else:
                    tag.name = newTag
                    tag.save()
        if n.tag_set.all().count() == 0 and newTag != '':
            tag = Tag(name = newTag)
            tag.save()
            tag.notes.add(n)

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