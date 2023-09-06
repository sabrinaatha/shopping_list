from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Sabrina Atha Shania',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
