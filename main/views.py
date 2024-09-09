from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Ryzen 3 3200G',
        'price': 1500000,
        'description': 'Ryzen 3 3200G is a processor that has 4 cores and 4 threads. It has a base clock of 3.6 GHz and a boost clock of 4.0 GHz. It is a good processor for gaming and productivity tasks.',
        'stock': 10
    }

    return render(request, "main.html", context)
