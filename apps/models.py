

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


MEDIA_TYPES = {
    r'^(jpg|jpeg|png|JPG)$': 'image',
}

FILE_TYPES = {
    r'^(pdf)$': 'documents',
}


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]

    for regex, folder in MEDIA_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            instance.type = folder
            return '%s/%s/%s' % (folder, instance._meta.model_name, file_type)
        except ValidationError:
            pass
    raise ValidationError('File type is unacceptable')


def file_type(instance, filename):
    file_type = filename.split('.')[-1]
    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            instance.type = folder
            return '%s/%s/%s' % (folder, instance._meta.model_name, file_type)
        except ValidationError:
            pass
    raise ValidationError('File type is unacceptable')


class Document(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_name)
    file = models.FileField(upload_to=file_type)
