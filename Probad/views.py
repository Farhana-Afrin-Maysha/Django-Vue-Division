from django.shortcuts import render
from .models import Division, District, Category, Chondokotha, Resturant
from django.http import JsonResponse


def home(request):
    return render(request, 'Probad/home.html')


def lazy_eagar(request):
    kotha = Chondokotha.objects.all()
    context = {
        "kotha": kotha
    }

    return render(request, "Probad/lazy.html", context)


def place(request):
    p1 = Resturant.objects.select_related()
    context = {
        "foods": p1
    }

    print(p1)
    return render(request, "Probad/resturant.html", context)


def about(request):
    return render(request, 'Probad/about.html')


def data(request):
    context = {
        'division': list(Division.objects.values()),
        'category': list(Category.objects.values()),

    }

    return JsonResponse(context, safe=False)


def chondokotha(request):
    queryAll = Chondokotha.objects.order_by('-id')
    if request.GET.get('district'):
        queryAll = queryAll.filter(district=request.GET.get('district'))
    if request.GET.get('division'):
        queryAll = queryAll.filter(district__division=request.GET.get('division'))
    if request.GET.get('category'):
        queryAll = queryAll.filter(category=request.GET.get('category'))

    chondokotha = queryAll.values('id', 'title', 'category', 'category__name', 'district', 'district__name',
                                  'district__division__name')
    context = {
        'chondokotha': list(chondokotha),

    }

    return JsonResponse(context, safe=False)


def district(request):
    print(request.GET)
    print('hello')
    queryAll = District.objects
    if request.GET.get('division'):
        queryAll = queryAll.filter(division=request.GET.get('division'))

    district = queryAll.values()
    data = {
        'district': list(district),

    }
    print(data)
    return JsonResponse(data, safe=False)
