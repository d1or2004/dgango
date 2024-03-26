from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Salom Diyor")


def about_page(request):
    return HttpResponse("Ma'lumot")