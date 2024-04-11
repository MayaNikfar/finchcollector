from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from django.views.generic import ListView
# from .models import Finch
# Create your views here.
finches =[
   {'name': 'Zebra', 'breed': 'Zebra Finch', 'description': 'These are small, sociable birds with distinctive black and white stripes on their chest'},
   {'name': 'Rainbow ', 'breed': 'Rainbow Finch', 'description': 'Also known as the Rainbow Finch, Gouldian Finches are prized for their stunning array of colors, including red, yellow, black, green, and blue. They are native to Australia and are considered endangered in the wild.'}  
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
   return render(request, 'finches/index.html', {
    'finches': finches
  })

# def finches_detail(request, finch_id):
#   finch = Finch.objects.get(id=finch_id)
#   return render(request, 'finchs/detail.html', {
#     'finch': finch
#   })

# class FinchCreate(CreateView):
#   model = Finch
#   fields = ['name', 'breed', 'description']
