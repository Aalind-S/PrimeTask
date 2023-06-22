from django.shortcuts import render
from .models import Restaurant
# Create your views here.

def search(request):
    if request.method == 'GET':
        
        try:
            query = request.GET['query']
            result = Restaurant.objects.filter(menu_items__icontains = query)
            context = {'result':result, 'query': query }
            return render(request, 'search.html', context)
        except:
            return render(request, 'search.html')
        
