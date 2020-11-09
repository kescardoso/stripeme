from django.shortcuts import render
from .models import Webdev


def all_webdevs(request):
    """ A view to show all webdevs from the web development portfolio """

    webdevs = Webdev.objects.all()

    context = {
        'webdevs': webdevs,
    }

    return render(request, 'webdevs/webdevs.html', context)
