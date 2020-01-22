from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
# Create your models here.

# class FileType(models.Model):

#     class TypeName(models.TextChoices):
#         EXCEL = '.xlsx', _('Excel File')
#         ERROR = '.error', _('Error File')
#         TEXT = '.txt', _('Text File')

#     type_name = models.CharField(
#         max_length=2,
#         choices=TypeName.choices,
#         default=TypeName.EXCEL
#     )    
class FileFieldForm(forms.Form):
    title = forms.CharField(max_length=50)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    upload_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<File: %s>' % self.title

# class InputFile(models.Model):

#     class TypeName(models.TextChoices):
#         EXCEL = '.xlsx', _('Excel File')
#         ERROR = '.error', _('Error File')
#         TEXT = '.txt', _('Text File')

#     file_name = models.CharField(max_length=50)
#     file_type = models.CharField(
#         max_length=8,
#         choices=TypeName.choices,
#         default=TypeName.EXCEL
#     )
#     upload_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     content = models.ForeignKey(FileContent, on_delete=models.DO_NOTHING)
#     create_time = models.DateField(auto_now_add=True)
#     last_update = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return '<File: %s>' % self.file_name