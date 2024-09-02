# Views artist 
from django.shortcuts import render, redirect
from django.http import Http404
from catalogue.models import Artist, Troupe
from catalogue.forms import ArtistTroupeForm

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    title = 'Liste des artistes'
    
    return render(request, 'artist/index.html', {
        'artists': artists,
        'title': title
    })

def show(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')
        
    title = 'Fiche d\'un artiste'

    troupe_affilie = artist.troupe

    #Il faut rafraichir la page pour voir le changement
    if request.method == 'POST':
        if request.user.is_superuser:
            form = ArtistTroupeForm(request.POST, instance=artist)
            if form.is_valid():
                form.save()  
    else:
        form = ArtistTroupeForm(instance=artist)

    return render(request, 'artist/show.html', {
        'artist': artist,
        'title': title,
        'troupe_affilie': troupe_affilie,
        'form': form,

    })