from catalogue.models import Show
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


#PDF des shows
def show_pdf(request):

    buf=io.BytesIO()

    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    textobj= c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    shows = Show.objects.all()
    lines = []

    for show in shows:
        #lines.append(show.id)
        lines.append('Nom: ' + show.title)
        lines.append('Location: ' + str(show.location))
        lines.append('Reservable: ' + str(show.bookable))
        lines.append('Prix: ' + str(show.price))
        lines.append(" ")

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='show.pdf')