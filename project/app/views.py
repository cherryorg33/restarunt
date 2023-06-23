from django.shortcuts import render
from app.models import Dish


def search_view(request):
    query = request.GET.get('query')
    if query:
        results = Dish.objects.filter(name__icontains=query)
    else:
        results = None
    return render(request, 'search.html', {'results': results})