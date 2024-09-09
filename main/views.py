from django.shortcuts import render

def show_main(request):
    products = [
        {
            'name' : 'Ryzen 3 3200G',
            'price': 1500000,
            'description': 'Ryzen 3 3200G is a processor that has 4 cores and 4 threads. It has a base clock of 3.6 GHz and a boost clock of 4.0 GHz. It is a good processor for gaming and productivity tasks.',
            'stock': 10
        },
        {
            'name' : 'Ryzen 5 3600',
            'price': 2500000,
            'description': 'Ryzen 5 3600 is a processor with 6 cores and 12 threads. It has a base clock of 3.6 GHz and a boost clock of 4.2 GHz.',
            'stock': 5
        },
        {
            'name' : 'Ryzen 7 3700X',
            'price': 4500000,
            'description': 'Ryzen 7 3700X has 8 cores and 16 threads with a base clock of 3.6 GHz and a boost clock of 4.4 GHz, suitable for high-end gaming and productivity.',
            'stock': 3
        },
        {
            'name' : 'Ryzen 5 5600',
            'price': 3500000,
            'description': 'Ryzen 5 5600 is a processor with 6 cores and 12 threads. It has a base clock of 3.7 GHz and a boost clock of 4.6 GHz.',
            'stock': 7
        },
        {
            'name' : 'Ryzen 9 5900X',
            'price': 7500000,
            'description': 'Ryzen 9 5900X has 12 cores and 24 threads with a base clock of 3.7 GHz and a boost clock of 4.8 GHz, suitable for high-end gaming and productivity.',
            'stock': 2
        },
        {
            'name' : 'Ryzen 9 5950X',
            'price': 9500000,
            'description': 'Ryzen 9 5950X has 16 cores and 32 threads with a base clock of 3.4 GHz and a boost clock of 4.9 GHz, suitable for high-end gaming and productivity.',
            'stock': 1
        },
        {
            'name' : 'Ryzen Threadripper 3960X',
            'price': 15000000,
            'description': 'Ryzen Threadripper 3960X has 24 cores and 48 threads with a base clock of 3.8 GHz and a boost clock of 4.5 GHz, suitable for high-end gaming and productivity.',
            'stock': 1
        },
        {
            'name' : 'Ryzen Threadripper 3970X',
            'price': 20000000,
            'description': 'Ryzen Threadripper 3970X has 32 cores and 64 threads with a base clock of 3.7 GHz and a boost clock of 4.5 GHz, suitable for high-end gaming and productivity.',
            'stock': 1
        }
    ]

    context = {
        'products': products
    }

    return render(request, "main.html", context)