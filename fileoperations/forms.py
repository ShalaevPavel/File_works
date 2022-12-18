from django.forms import ModelForm
from .models import File, FileBuilder

class FileForm(ModelForm):

    class Meta:
        model = File
        fields = "__all__"


class FileBuilderForm(ModelForm):

        class Meta:
            model = FileBuilder
            fields = "__all__"