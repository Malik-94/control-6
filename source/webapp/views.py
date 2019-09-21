from django.shortcuts import render,get_list_or_404
from webapp.models import Book


def index_view(request):
    # здесь нужно поставить правильный филтьр
    # и сортировку вместо all()
    #book = Book.objects.order_by('category', 'name')
    book = Book.objects.all()
    return render(request, 'index.html', context={
        'book': book
    })

