#EA PDF TEST
from catalogue.models import Artist
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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