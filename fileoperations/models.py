from django.db import models


# Create your models here.

class File(models.Model):
    input_file = models.FileField(upload_to='input_files/')
    output_file = models.FileField(upload_to='output_files/')

    def __str__(self):
        return self.input_file.name


class FileBuilder(models.Model):
    input_file = models.CharField(max_length=255)
    output_file = models.CharField(max_length=255)
    file_type = models.CharField(max_length=5)
    is_zipped = models.BooleanField(default=False)
    is_encrypted = models.BooleanField(default=False)
    key_file = models.CharField(blank=True, max_length=255)

    def serialize(self):
        return {
            "input_file": self.input_file,
            "output_file": self.output_file,
            "file_type": self.file_type,
            "is_zipped": self.is_zipped,
            "is_encrypted": self.is_encrypted,
            "key_file": self.key_file
        }

    def __str__(self):
        return self.input_file + " to " + self.output_file
