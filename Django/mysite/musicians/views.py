from django.shortcuts import render , redirect,  get_object_or_404
from .forms import MusicianForm, AlbumForm
from .models import Musician,Album,Music
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    musicians = Musician.objects.all()
    context = {
        'musicians' : musicians
    }
    return render(request, 'musicians/index.html', context)

def create(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:index')
    else:
        form = MusicianForm()
        print(form)
    context = {
        'form':form,
    }
    return render(request, 'musicians/create.html',context)


def detail(request, musician_pk):
    musician = Musician.objects.get(pk = musician_pk)
    albums = Album.objects.filter(musician=musician).order_by('-created_at')
    musics = Music.objects.filter(album__in=albums)
    print(musics)
    context = {
        'musician': musician,
        'albums':albums,
        'musics':musics
    }
    return render(request,'musicians/detail.html' , context)


def update(request, musician_pk):
    musician = get_object_or_404(Musician, id = musician_pk)
    if request.method == "POST":
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            movie = form.save()
            return redirect('musicians:index')
    else:
        form = MusicianForm(instance=musician)
    context = {
        'form': form,
    }
    return render(request, 'musicians/create.html',context)

def delete(request,musician_pk):
    if request.method == "POST":
        musician = get_object_or_404(Musician, id = musician_pk)
        musician.delete()
    return redirect('musicians:index')



def album_create(request,musician_pk):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album = album_form.save(commit=False)
            musician = Musician.objects.get(pk=musician_pk)
            album.musician=musician
            album.save()
            return redirect('musicians:detail',musician_pk)
    else:
        album_form = AlbumForm()
    context = {
        'album_form':album_form,
    }
    return render(request, 'musicians/album_create.html',context)