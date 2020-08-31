from django.shortcuts import render

from .models import Design


def all_designs(request):
    """ A view to show all designs from the design portfolio """

    designs = Design.objects.all()

    context = {
        'designs': designs,
    }

    return render(request, 'designs/designs.html', context)
