from django.shortcuts import render

def show_main(request):
    context = {
        'application_name' : 'Amajon',
        'nama': 'Athallah Damar Jiwanto',
        'npm': '2306245024',
        'kelas': 'PBP D',
    }

    return render(request, "main.html", context)
