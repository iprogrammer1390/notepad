from multiprocessing import context
from django.shortcuts import render
from .models import Note

def note_list_view(request):
    notes = Note.objects.all()
    context={
        'notes':notes,
    }
    return render(request, 'note_list.html', context)
