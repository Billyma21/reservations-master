# models artist
from django.db import models

#API Auth & Permissions (pygments)
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Artist(models.Model):
    #Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_artiste")
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    def __str__(self):
        return self.firstname +" "+ self.lastname
    
    class Meta:
        db_table = "artists"

'''
    #API Auth & Permissions
    owner = models.ForeignKey('auth.User', related_name='artists', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        options = {'firstname'+" "+'lastname': self.firstname +" "+ self.lastname} if self.firstname +" "+ self.lastname else {}
        formatter = HtmlFormatter(full=True, **options)
        self.highlighted = highlight(lexer, formatter)
        super().save(*args, **kwargs)
'''