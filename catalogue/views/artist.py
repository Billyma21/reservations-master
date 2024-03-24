# Views artist 
from django.shortcuts import render
from django.http import Http404

from catalogue.models import Artist


#EA PDF TEST
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
    
    return render(request, 'artist/show.html', {
        'artist': artist,    
        'title': title 
    })

#protoype pdf dl
def artist_pdf(request):

    buf=io.BytesIO()

    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    textobj= c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    artists = Artist.objects.all()

    lines = []

    for artist in artists:
        #lines.append(artist.id)
        lines.append(artist.firstname)
        lines.append(artist.lastname)
        lines.append(" ")


    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='artist.pdf')