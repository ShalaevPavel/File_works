from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import FileForm, FileBuilderForm
from .models import File, FileBuilder
from .utils import calculate_math_expressions, Builder


# Create your views here.

def index(request):
    return render(request, 'index.html')


def encrypt(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = FileForm()
    return render(request, 'encrypt.html', {'form': form})


def debug_page(request):
    text_ = "Hello World"
    objs = File.objects.all()
    return render(request, 'debug.html', {"objs": objs, "text_": text_})


def build(request):
    content = ""
    if request.method == 'POST':
        form = FileBuilderForm(request.POST)
        if form.is_valid():
            # file is saved
            form.save()
            file_builder = form.instance
            cl = Builder(file_builder.input_file, file_builder.output_file,
                         file_builder.file_type, file_builder.is_zipped, file_builder.is_encrypted,
                         file_builder.key_file)
            file_ = cl.build()
            content = calculate_math_expressions(file_.read())
            # cl.build().write(calculate_math_expressions(cl.build().read()))
            # return HttpResponseRedirect(reverse("index"))
            file_.write(content)
            return HttpResponse(content)
    else:
        form = FileBuilderForm()

    return render(request, 'build.html', {'form': form, "content": content})


def api_file(request, file_id):
    file = FileBuilder.objects.get(id=file_id)
    return JsonResponse({"file": file.serialize()})

