from django.shortcuts import render, get_object_or_404
from .models import Webdev


def all_webdevs(request):
    """ A view to show all webdevs from the web development portfolio """

    webdevs = Webdev.objects.all()

    context = {
        'webdevs': webdevs,
    }

    return render(request, 'webdevs/webdevs.html', context)


def webdev_detail(request, webdev_id):
    """ A view to show individual webdev details """

    webdev = get_object_or_404(Webdev, pk=webdev_id)

    context = {
        'webdev': webdev,
    }

    return render(request, 'webdevs/webdev_detail.html', context)
