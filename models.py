from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class filecompare(models.Model):
    Originalfile = models.FileField(upload_to='generic/', verbose_name= 'ORIGINAL FILE : ')
    Comparedfile = models.FileField(upload_to='compared/', verbose_name= 'FILE TO COMPARE : ')

    def __str__(self) :
        return str(self.Originalfile)


class wrd_to_pdf(models.Model):
    Wordfile = models.FileField(upload_to='doctopdf/', validators=[FileExtensionValidator(allowed_extensions=["doc", "docx"])], verbose_name= 'WORD FILE :')

    def __str__(self) :
        return str(self.Wordfile)
    

