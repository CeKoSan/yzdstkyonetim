
from django.shortcuts import render
from .forms import KayitForm

def ana_sayfa(request):
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tesekkur.html')
    else:
        form = KayitForm()
    return render(request, 'form.html', {'form': form})
