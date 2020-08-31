from django.shortcuts import render, get_object_or_404
from .models import Design


def all_designs(request):
    """ A view to show all designs from the design portfolio """

    designs = Design.objects.all()

    context = {
        'designs': designs,
    }

    return render(request, 'designs/designs.html', context)


def design_detail(request, design_id):
    """ A view to show individual design details """

    design = get_object_or_404(Design, pk=design_id)

    context = {
        'design': design,
    }

    return render(request, 'designs/design_detail.html', context)
